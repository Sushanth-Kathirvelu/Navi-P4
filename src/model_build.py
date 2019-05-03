# Script reads train and test files from tier-3 and implements ML techniques on them
# Script Reference :
# https://www.kaggle.com/jsaguiar/lightgbm-with-simple-features

#import argparse
import operator
import pandas as pd
#import os
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def kfold_lightgbm(
        train_df,
        test_df,
        num_folds,
        stratified=False,
        debug=False):

    # Cross validation model
    if stratified:
        folds = StratifiedKFold(
            n_splits=num_folds,
            shuffle=True,
            random_state=1001)
    else:
        folds = KFold(n_splits=num_folds, shuffle=True, random_state=1001)
    # Create arrays and dataframes to store results
    oof_preds = np.zeros(train_df.shape[0])
    sub_preds = np.zeros(test_df.shape[0])
    feature_importance_df = pd.DataFrame()
    feats = [
        f for f in train_df.columns if f not in [
            'TARGET',
            'SK_ID_CURR',
            'SK_ID_BUREAU',
            'SK_ID_PREV',
            'index']]

    for n_fold, (train_idx, valid_idx) in enumerate(
            folds.split(train_df[feats], train_df['TARGET'])):
        train_x, train_y = train_df[feats].iloc[train_idx], train_df['TARGET'].iloc[train_idx]
        valid_x, valid_y = train_df[feats].iloc[valid_idx], train_df['TARGET'].iloc[valid_idx]

        # LightGBM parameters found by Bayesian optimization
        clf = LGBMClassifier(
            nthread=4,
            n_estimators=10000,
            learning_rate=0.02,
            num_leaves=34,
            colsample_bytree=0.9497036,
            subsample=0.8715623,
            max_depth=8,
            reg_alpha=0.041545473,
            reg_lambda=0.0735294,
            min_split_gain=0.0222415,
            min_child_weight=39.3259775,
            silent=-1,
            verbose=-1, )

        clf.fit(
            train_x,
            train_y,
            eval_set=[
                (train_x,
                 train_y),
                (valid_x,
                 valid_y)],
            eval_metric='auc',
            verbose=200,
            early_stopping_rounds=200)

        oof_preds[valid_idx] = clf.predict_proba(
            valid_x, num_iteration=clf.best_iteration_)[:, 1]
        sub_preds += clf.predict_proba(test_df[feats],
                                       num_iteration=clf.best_iteration_)[:,
                                                                          1] / folds.n_splits

        fold_importance_df = pd.DataFrame()
        fold_importance_df["feature"] = feats
        fold_importance_df["importance"] = clf.feature_importances_
        fold_importance_df["fold"] = n_fold + 1
        feature_importance_df = pd.concat(
            [feature_importance_df, fold_importance_df], axis=0)
        print(
            'Fold %2d AUC : %.6f' %
            (n_fold +
             1,
             roc_auc_score(
                 valid_y,
                 oof_preds[valid_idx])))
        del clf, train_x, train_y, valid_x, valid_y

    print('Full AUC score %.6f' % roc_auc_score(train_df['TARGET'], oof_preds))
    # Write submission file and plot feature importance
    if not debug:
        test_df['TARGET'] = sub_preds
        test_df[['SK_ID_CURR', 'TARGET']].to_csv(
            dir + submission_file_name, index=False)
    display_importances(feature_importance_df)
    return feature_importance_df

# Display/plot feature importance


def display_importances(feature_importance_df_):
    cols = feature_importance_df_[["feature", "importance"]].groupby(
        "feature").mean().sort_values(by="importance", ascending=False)[:40].index
    best_features = feature_importance_df_.loc[feature_importance_df_.feature.isin(
        cols)]
    plt.figure(figsize=(8, 10))
    sns.barplot(
        x="importance",
        y="feature",
        data=best_features.sort_values(
            by="importance",
            ascending=False))
    plt.title('LightGBM Features (avg over folds)')
    plt.tight_layout()
    plt.savefig('lgbm_importances01.png')


dir = "/Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4"
tier3_loc = dir + "/tier3/"

train = "application_train.csv"
test = "application_test.csv"
submission_file_name = "sub_lgbm.csv"


# Reading train dataset
train_df = pd.read_csv(tier3_loc + train)
train_df.shape

# Reading test dataset
test_df = pd.read_csv(tier3_loc + test)
test_df.shape

# Dropping prev_id as it is not needed for the join
#train_df.drop(['SK_ID_CURR'],axis =1,inplace=True)
#test_df.drop(['SK_ID_CURR'],axis =1,inplace=True)

#X_train = train_df.loc[:, train_df.columns != 'TARGET']
#y_train = train_df['TARGET']

feat_importance = kfold_lightgbm(
    train_df,
    test_df,
    num_folds=7,
    stratified=False,
    debug=False)


train_df.fillna(-999, inplace=True)

rf = RandomForestClassifier(
    n_estimators=50,
    max_depth=8,
    min_samples_leaf=4,
    max_features=0.5)
rf.fit(train_df.drop(['TARGET', 'SK_ID_CURR'], axis=1), train_df['TARGET'])
old_features = list(train_df.drop(['SK_ID_CURR', 'TARGET'], axis=1))
feature_importances = {}
feature_importances_list = rf.feature_importances_
for index, feature in enumerate(old_features):
    feature_importances[feature] = feature_importances_list[index]
itemlist = sorted(
    feature_importances.items(),
    key=operator.itemgetter(1),
    reverse=True)

fig, ax = plt.subplots()
feature_names = [x[0] for x in itemlist[:20]]
feature_importance = [x[1] for x in itemlist[:20]]

ax.barh(feature_names, feature_importance, align='center')
ax.set_yticklabels(feature_names)
ax.invert_yaxis()
ax.set_xlabel('Importance')
ax.set_title('Feature Importance')

plt.show()
