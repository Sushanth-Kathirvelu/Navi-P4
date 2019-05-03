import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import featuretools as ft
import os


def read_data(path):
    """
    This function loads the data.
    Parameters
    ----------
    path : str
        The path to the input data.
    Returns
    ----------
    combine_df : pandas dataframe
        The combined train and test set.
    bureau_df : pandas dataframe
        The Credit Bureau data.
    bureau_balance_df : pandas dataframe
        The Credit Bureau monthly balance data.
    pos_cash_df : pandas dataframe
        The POS and cash loans data.
    credit_card_df : pandas dataframe
        The credit card monthly balance data.
    previous_application_df : pandas dataframe
        The previous applications for loans data.
    installments_payments_df : pandas dataframe
        The repayment history data.
    """
    if path[-1] == '/':
        path = path[:-1]

    train_df = pd.read_csv(path + '/application_train.csv')
    test_df = pd.read_csv(path + '/application_test.csv')
    bureau_df = pd.read_csv(path + '/bureau.csv')
    bureau_balance_df = pd.read_csv(path + '/bureau_balance.csv')
    pos_cash_df = pd.read_csv(path + '/POS_CASH_balance.csv')
    credit_card_df = pd.read_csv(path + '/credit_card_balance.csv')
    previous_application_df = pd.read_csv(path + '/previous_application.csv')
    installments_payments_df = pd.read_csv(path + '/installments_payments.csv')

    test_df["TARGET"] = -999
    combine_df = train_df.append(test_df, ignore_index=True)

    return combine_df, bureau_df, bureau_balance_df, pos_cash_df, \
        credit_card_df, previous_application_df, installments_payments_df


def create_feature_matrix(
        combine_df,
        bureau_df,
        bureau_balance_df,
        pos_cash_df,
        credit_card_df,
        previous_application_df,
        installments_payments_df,
        primitive_set):
    """
    This function use Deep Feature Synthesis to create new features.
    @https://docs.featuretools.com/index.html
    @Deep Feature Synthesis: Towards Automating Data Science Endeavors
    Parameters
    ----------
    combine_df : pandas dataframe
        The combined train and test set.
    bureau_df : pandas dataframe
        The Credit Bureau data.
    bureau_balance_df : pandas dataframe
        The Credit Bureau monthly balance data.
    pos_cash_df : pandas dataframe
        The POS and cash loans data.
    credit_card_df : pandas dataframe
        The credit card monthly balance data.
    previous_application_df : pandas dataframe
        The previous applications for loans data.
    installments_payments_df : pandas dataframe
        The repayment history data.
    primitive_set : str
        If some or all of the primitives should be used
    Returns
    ----------
    train_df : pandas dataframe
        The newly created training dataset.
    test_df : pandas dataframe
        The newly created testing dataset.
    """


    #Here we create Entities and specify their relations.
    #@https://docs.featuretools.com/index.html for more info.
    es = ft.EntitySet(id='dsp')

    es = es.entity_from_dataframe(
        entity_id='combine',
        dataframe=combine_df,
        index='SK_ID_CURR')
    es = es.entity_from_dataframe(
        entity_id='bureau',
        dataframe=bureau_df,
        index='SK_ID_BUREAU')
    es = es.entity_from_dataframe(
        entity_id='bureau_balance',
        dataframe=bureau_balance_df,
        make_index=True,
        index='new_bureau_balance_index')
    es = es.entity_from_dataframe(entity_id='pos_cash', dataframe=pos_cash_df,
                                  make_index=True, index='new_pos_cash_index')
    es = es.entity_from_dataframe(
        entity_id='credit_card',
        dataframe=credit_card_df,
        make_index=True,
        index='new_credit_card_index')
    es = es.entity_from_dataframe(
        entity_id='previous_application',
        dataframe=previous_application_df,
        index='SK_ID_PREV')
    es = es.entity_from_dataframe(
        entity_id='installments_payments',
        dataframe=installments_payments_df,
        make_index=True,
        index='installments_index')

    relations = {}

    relations['combine_bureau'] = ft.Relationship(
        es['combine']['SK_ID_CURR'], es['bureau']['SK_ID_CURR'])
    relations['bureau__bureau_balance'] = ft.Relationship(
        es['bureau']['SK_ID_BUREAU'], es['bureau_balance']['SK_ID_BUREAU'])
    relations['combine__previous_application'] = ft.Relationship(
        es['combine']['SK_ID_CURR'], es['previous_application']['SK_ID_CURR'])
    relations['previous_application__pos_cash'] = ft.Relationship(
        es['previous_application']['SK_ID_PREV'], es['pos_cash']['SK_ID_PREV'])
    relations['previous_application__installments_payments'] = ft.Relationship(
        es['previous_application']['SK_ID_PREV'],
        es['installments_payments']['SK_ID_PREV'])
    relations['previous_application__credit_card'] = ft.Relationship(
        es['previous_application']['SK_ID_PREV'],
        es['credit_card']['SK_ID_PREV'])

    es = es.add_relationships(list(relations.values()))

    #Here we perform DFS with subset of feature primitives.
    if primitive_set == 'some':
        feature_matrix, feature_defs = ft.dfs(
            entityset=es, target_entity='combine', agg_primitives=[
                'sum', 'count', 'min', 'max', 'mean', 'mode'],
            trans_primitives=[], max_depth=2, verbose=True)

    #Here we perform DFS with all default feature primitives.
    elif primitive_set == 'all':
        feature_matrix, feature_defs = ft.dfs(
            entityset=es, target_entity='combine', agg_primitives=[
                'sum', 'std', 'max', 'skew', 'min', 'mean', 'count',
                'percent_true', 'n_unique', 'mode'],
            trans_primitives=['day', 'year', 'month', 'weekday',
                              'haversine', 'num_words', 'num_characters'],
            max_depth=2, verbose=True)

    train_df = feature_matrix[feature_matrix['TARGET'] != -999]
    test_df = feature_matrix[feature_matrix['TARGET'] == -999]

    train_df = train_df.reset_index()
    test_df = test_df.reset_index()

    return train_df, test_df


def feature_select(train_df, test_df, importance_threshold):
    """
    This function selects features based
    on their importance.
    Parameters
    ----------
    train_df : pandas dataframe
        The previously created training dataset.
    test_df : pandas dataframe
        The previously created testing dataset.
    importance_threshold : float
        The threshold to select features. Defauts to 0.
    Returns
    ----------
    train_df : pandas dataframe
        The newly created training dataset.
    test_df : pandas dataframe
        The newly created testing dataset.
    """
    train_df = pd.get_dummies(train_df)
    test_df = pd.get_dummies(test_df)
    train_df.fillna(-999, inplace=True)
    test_df.fillna(-999, inplace=True)

    rf = RandomForestClassifier()
    rf.fit(train_df.drop(['TARGET', 'SK_ID_CURR'], axis=1), train_df['TARGET'])
    old_features = list(train_df.drop(['SK_ID_CURR', 'TARGET'], axis=1))
    feature_importances = {}
    feature_importances_list = rf.feature_importances_
    for index, feature in enumerate(old_features):
        feature_importances[feature] = feature_importances_list[index]

    #Saving only features with importance higher than threshold.
    new_features = []
    for feature in feature_importances:
        if feature_importances[feature] > importance_threshold:
            new_features.append(feature)

    new_features.append('SK_ID_CURR')
    new_features.append('TARGET')

    #Making sure train and test have same features.
    #This is required due to one hot encoding.
    feat_list = [k for k in new_features if k in test_df.columns]
    train_df = train_df[feat_list]
    test_df = test_df[feat_list]

    train_df, test_df = train_df.align(test_df, join='inner', axis=1)

    return train_df, test_df


def load_feature_matrix(
        path,
        primitive_set,
        importance_threshold,
        tier3_loc,
        train_write,
        test_write):
    """
    This function creates the training and
    testing feature matrices.
    Parameters
    ----------
    path : str
        Path to the data folder.
    primitive_set : str
        If some or all of the primitives should be used
    importance_threshold : float
        The threshold to select features. Defauts to 0.
    tier3_loc : str
        Tier-3 location
    train_write : str
        Train file name to write into tier-3
    test_write : str
        Test file name to write into tier-3

    Returns
    ----------
    final_train : pandas dataframe
        The final training dataset.
    final_test : pandas dataframe
        The final testing dataset.

    """

    # Checking if tier-3 exists, if not, then creating
    if not os.path.isdir(tier3_loc):
        print("Creating tier-3 folder")
        os.mkdir(tier3_loc)

    combine_df, bureau_df, bureau_balance_df, pos_cash_df, credit_card_df, \
        previous_application_df, installments_payments_df = read_data(path)

    train_df, test_df = create_feature_matrix(combine_df, bureau_df,
                                              bureau_balance_df, pos_cash_df,
                                              credit_card_df,
                                              previous_application_df,
                                              installments_payments_df,
                                              primitive_set)
    final_train, final_test = feature_select(
        train_df, test_df, importance_threshold)

    # Saving to disk.
    final_train.to_csv(path_or_buf=tier3_loc + train_write, index=False)
    final_test.to_csv(path_or_buf=tier3_loc + test_write, index=False)
