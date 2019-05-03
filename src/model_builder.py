# Script Reference :
# https://www.kaggle.com/jsaguiar/lightgbm-with-simple-features

import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import roc_auc_score
import numpy as np
import os


def kfold_lightgbm(
        train_df,
        test_df,
        submission_file_name,
        path,
        stratified=False,
        num_folds=5):
    """
    Applies k-fold cross validation with gbm to train the model and
    predicts on the test set. Writes submission file also.
    Parameters
    ----------
    train_df : pandas dataframe
        Training dataframe
    test_df : pandas dataframe
        Test dataframe
    submission_file_name : str
        Name of the submission file
    path : str
        Project directory path
    stratified : bool
        If stratified sampling should be used or not
    num_folds : int
        Number of folds to use for cross validation
    """

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
    feats = [
        f for f in train_df.columns if f not in [
            'TARGET',
            'SK_ID_CURR',
            'SK_ID_BUREAU',
            'SK_ID_PREV',
            'index']]

    for n_fold, (train_idx, valid_idx) in enumerate(
            folds.split(train_df[feats], train_df['TARGET'])):
        train_x, train_y = train_df[feats].iloc[train_idx], \
            train_df['TARGET'].iloc[train_idx]
        valid_x, valid_y = train_df[feats].iloc[valid_idx], \
            train_df['TARGET'].iloc[valid_idx]

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
            verbose=-1)

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
                     num_iteration=clf.best_iteration_)[:, 1] / folds.n_splits

        fold_importance_df = pd.DataFrame()
        fold_importance_df["feature"] = feats
        fold_importance_df["importance"] = clf.feature_importances_
        fold_importance_df["fold"] = n_fold + 1
        print(
            'Fold %2d AUC : %.6f' %
            (n_fold +
             1,
             roc_auc_score(
                 valid_y,
                 oof_preds[valid_idx])))
        del clf, train_x, train_y, valid_x, valid_y

    print('Full AUC score %.6f' % roc_auc_score(train_df['TARGET'], oof_preds))
    test_df['TARGET'] = sub_preds
    test_df[['SK_ID_CURR', 'TARGET']].to_csv(
        path + submission_file_name, index=False)


def model_train(
        path,
        tier3_loc,
        train_write,
        test_write,
        submission_file_name):
    """
    Reads train, test files from tier-3 and implements ML techniques on them.
    Parameters
    ----------
    path : str
        Project directory path
    tier3_loc : str
        Tier-3 location
    train_write : str
        Train file name to write into tier-3
    test_write : str
        Test file name to write into tier-3
    submission_file_name : str
        Name of the submission file
    """
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

    # Reading train dataset
    train_df = pd.read_csv(tier3_loc + train_write)

    # Reading test dataset
    test_df = pd.read_csv(tier3_loc + test_write)

    kfold_lightgbm(
        train_df,
        test_df,
        submission_file_name,
        path,
        stratified=False,
        num_folds=5)
