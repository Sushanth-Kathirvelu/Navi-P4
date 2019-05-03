# Script reads all files from tier-2,joins them based on keys, and saves
# to tier-3

import pandas as pd
import os
import sys


def file_check(tier2_loc, file):
    """
    Check if a file is present in tier-2 and return true, else raise exception
    Parameters
    ----------
    tier2_loc : str
        Tier-2 location
    file : str
        Name of the file
    Returns
    ----------
    bool : bool
        True if file is present
    """
    # Basic checks to see if all required files are present in tier-1
    if not os.path.isfile(tier2_loc + file):
        print(file + " is missing in tier-2, please check and re-run")
        sys.exit(0)

    return True


def perform_joins(df, bureau_df, pa, pcb, ip, ccb):
    """
    Performs joins on the input dataframe according to the data model.
    Parameters
    ----------
    df : pandas dataframe
        dataframe to be joined
    bureau: pandas dataframe
        bureau dataframe
    pa : pandas dataframe
        previous_application dataframe
    pcb : pandas dataframe
        pos cash balance dataframe
    ip : pandas dataframe
        installments payments dataframe
    ccb: pandas dataframe
        credit card balance dataframe
    Returns
    ----------
    df : pandas dataframe
        final dataframe after performing all joins
    """
    df = df.join(bureau_df, how='left', on='SK_ID_CURR', rsuffix='bb')
    df = df.join(pa, how='left', on='SK_ID_CURR', rsuffix='pa')
    df = df.join(pcb, how='left', on='SK_ID_CURR', rsuffix='pcb')
    df = df.join(ip, how='left', on='SK_ID_CURR', rsuffix='ip')
    df = df.join(ccb, how='left', on='SK_ID_CURR', rsuffix='ccb')
    return df


def tier3_loader(
        tier2_loc,
        tier3_loc,
        train_write,
        test_write,
        train,
        test,
        previous_application,
        bureau,
        bureau_balance,
        credit_card_balance,
        installments_payments,
        pos_cash_balance):
    """
    """

    # Checking if the tier-2 directory is present in the project directory
    if not os.path.isdir(tier2_loc):
        print("Tier-2 folder not present, create using tier2_load.py")
        sys.exit()

    # Checking if tier-3 exists, if not, then creating
    if not os.path.isdir(tier3_loc):
        print("Creating tier-3 folder")
        os.mkdir(tier3_loc)

    # Checking if all the files are present in tier-2
    if file_check(tier2_loc, train) and \
            file_check(tier2_loc, test) and \
            file_check(tier2_loc, previous_application) and \
            file_check(tier2_loc, bureau) and \
            file_check(tier2_loc, bureau_balance) and \
            file_check(tier2_loc, credit_card_balance) and \
            file_check(tier2_loc, installments_payments) and \
            file_check(tier2_loc, pos_cash_balance):

        # Reading all data files
        train_df = pd.read_csv(tier2_loc + train)
        test_df = pd.read_csv(tier2_loc + test)
        pa = pd.read_csv(tier2_loc + previous_application)
        b = pd.read_csv(tier2_loc + bureau)
        bb = pd.read_csv(tier2_loc + bureau_balance)
        ccb = pd.read_csv(tier2_loc + credit_card_balance)
        ip = pd.read_csv(tier2_loc + installments_payments)
        pcb = pd.read_csv(tier2_loc + pos_cash_balance)

        # Joining bureau balance and bureau on SK_ID_BUREAU
        bureau_df = b.join(bb, how='left', on='SK_ID_BUREAU')
        bureau_df.drop(['SK_ID_BUREAU'], axis=1, inplace=True)

        # Performing joins on train and test data
        train_set = perform_joins(train_df, bureau_df, pa, pcb, ip, ccb)
        test_set = perform_joins(test_df, bureau_df, pa, pcb, ip, ccb)

        # Saving
        train_set.to_csv(path_or_buf=tier3_loc + train_write, index=False)
        test_set.to_csv(path_or_buf=tier3_loc + test_write, index=False)
