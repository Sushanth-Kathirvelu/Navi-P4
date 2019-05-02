#Script reads all files from tier-1, 
#applies required transformations, 
#and saves to tier-2

#import argparse
import pandas as pd
import os
import copy
import sys

#Directory of folder location
dir = "/Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4"
tier2_loc = dir+"/tier2/"
tier1_loc = dir+"/tier1/"

#Names of all raw csv files
credit_card_balance = "credit_card_balance.csv"
installments_payments = "installments_payments.csv"
pos_cash_balance = "POS_CASH_balance.csv"
bureau = "bureau.csv"
bureau_balance = "bureau_balance.csv"
previous_application = "previous_application.csv"
train = "application_train.csv"
test = "application_test.csv"


def file_check(tier1_loc,file):
    """
    Check if a file is present in tier-1 and return true, else raise exception
    Parameters
    ----------
    tier1_loc : str
        Tier-1 location
    file : str
        Name of the file
    Returns
    ----------
    bool : bool
        True if file is present
    """
    #Basic checks to see if all required files are present in tier-1
    if not os.path.isfile(tier1_loc+file):
        print(file+" is missing in tier-1, please check and re-run")
        #raise FileNotFoundError(file+" is missing in tier-1")
        sys.exit(0)
        
    return True

def one_hot_encoder(df, nan_as_category = True):
    """
    This function converts the categorical columns 
    of any pandas dataframe into dummies
    Parameters
    ----------
    df : pandas dataframe
        Any pandas dataframe
    nan_as_category : boolean
        If nan should be considered as a categorical level or not
    Returns
    ----------
    df : pandas dataframe
        Dataframe with all categorical columns converted to dummies
    """
    
    #Generating list of categorical columns
    categorical_columns = [col for col in df.columns if df[col].dtype == 'object']
    #Converting to dummies
    df = pd.get_dummies(df, columns= categorical_columns, dummy_na= nan_as_category)   
    return df

def train_test_ltw(tier1_loc,train,test,tier2_loc):
    """
    This function loads data from tier-1,applies transformations,
    and writes the train and test data to tier-2.
    Parameters
    ----------
    tier1_loc : str
        The path to the tier-1 location where the data is read from.
    train : str
        The name of the train file.
    test : str
        The name of the test file.
    tier2_loc : str
        The path to the tier-2 location where the transformed data is saved.
    """
    if file_check(tier1_loc,train) and file_check(tier1_loc,test):
        #Reading train dataset
        train_df = pd.read_csv(tier1_loc+train)    
        #Reading test dataset
        test_df = pd.read_csv(tier1_loc+test)
        #Length of training set
        train_objs_num = len(train_df)
        #Joining train and test to perform tranformations
        dataset = pd.concat(objs=[train_df, test_df], axis=0,sort=False)
        #One hot encoding for all categorical columns
        dataset = one_hot_encoder(dataset, nan_as_category= True)
        #Removing any constant columns
        dataset = dataset.loc[:, (dataset != dataset.iloc[0]).any()] 
        #Splitting back into train and test
        train_df = copy.copy(dataset[:train_objs_num])
        test_df = copy.copy(dataset[train_objs_num:])
        #Dropping prev_id as it is not needed for the join
        test_df.drop(['TARGET'],axis =1,inplace=True)
        #Deleting intermediate dataframes
        del dataset,train_objs_num
        #Saving Train and Test
        train_df.to_csv(path_or_buf = tier2_loc+train,index=False)
        test_df.to_csv(path_or_buf = tier2_loc+test,index=False)

def previous_application_ltw(tier1_loc,previous_application,tier2_loc):
    """
    This function loads previous application data from tier-1,
    applies transformations, and writes the data to tier-2.
    Parameters
    ----------
    tier1_loc : str
        The path to the tier-1 location where the data is read from.
    previous_application : str
        The name of the previous application file.
    tier2_loc : str
        The path to the tier-2 location where the transformed data is saved.
    """
    if file_check(tier1_loc,previous_application):
        #Reading previous_application.csv
        pa = pd.read_csv(tier1_loc+previous_application)
        #Dropping prev_id as it is not needed for the join
        pa.drop(['SK_ID_PREV'],axis =1,inplace=True)
        #One hot encoding for all categorical columns
        pa = one_hot_encoder(pa, nan_as_category= True)
        #Aggregating all columns based on SK_ID_CURR
        pa_agg = pa.groupby('SK_ID_CURR').agg(['min','max','mean','var'])
        #Cleaning column names after aggregation
        pa_agg.columns = pd.Index(['pa_' + e[0] + "_" + e[1] for e in pa_agg.columns.tolist()])
        #Getting count of credit accounts for each unique ID
        pa_agg['pa_count'] = pa.groupby('SK_ID_CURR').size()     
        #Deleting intermediate dataframes
        del pa
        #Removing any constant columns
        pa_agg = pa_agg.loc[:, (pa_agg != pa_agg.iloc[0]).any()] 
        #Saving
        pa_agg.to_csv(path_or_buf = tier2_loc+previous_application,index=False)


def bureau_ltw(tier1_loc,bureau,tier2_loc):
    """
    This function loads bureau data from tier-1,applies transformations,
    and writes the data to tier-2.
    Parameters
    ----------
    tier1_loc : str
        The path to the tier-1 location where the data is read from.
    bureau : str
        The name of the bureau file.
    tier2_loc : str
        The path to the tier-2 location where the transformed data is saved.
    """
    
    if file_check(tier1_loc,bureau):
        #Reading bureau.csv
        b = pd.read_csv(tier1_loc+bureau)
        #One hot encoding for all categorical columns
        b = one_hot_encoder(b, nan_as_category= True)
        #Removing any constant columns
        b = b.loc[:, (b != b.iloc[0]).any()] 
        #Saving
        b.to_csv(path_or_buf = tier2_loc+bureau,index=False)


def bureau_balance_ltw(tier1_loc,bureau_balance,tier2_loc):
    """
    This function loads bureau balance data from tier-1,applies transformations,
    and writes the data to tier-2.
    Parameters
    ----------
    tier1_loc : str
        The path to the tier-1 location where the data is read from.
    bureau_balance : str
        The name of the bureau balance file.
    tier2_loc : str
        The path to the tier-2 location where the transformed data is saved.
    """
    
    if file_check(tier1_loc,bureau_balance):
        #Reading bureau balance
        bb = pd.read_csv(tier1_loc+bureau_balance)
        #One hot encoding for all categorical columns
        bb = one_hot_encoder(bb, nan_as_category= True)
        #Aggregating all columns based on SK_ID_CURR
        bb_agg = bb.groupby('SK_ID_BUREAU').agg(['min','max','mean','var'])
        #Cleaning column names after aggregation
        bb_agg.columns = pd.Index(['bb_' + e[0] + "_" + e[1] for e in bb_agg.columns.tolist()])
        #Getting count of credit accounts for each unique ID
        bb_agg['bb_count'] = bb.groupby('SK_ID_BUREAU').size()
        #Deleting intermediate dataframes
        del bb
        #Removing any constant columns    
        bb_agg = bb_agg.loc[:, (bb_agg != bb_agg.iloc[0]).any()] 
        #Saving
        bb_agg.to_csv(path_or_buf = tier2_loc+bureau_balance,index=False)


##############################################################################################
#Reading and pre-processing credit_card_balance.csv
##############################################################################################
def ccb_ltw(tier1_loc,credit_card_balance,tier2_loc):
    """
    This function loads credit card balance data from tier-1,
    applies transformations,and writes the data to tier-2.
    Parameters
    ----------
    tier1_loc : str
        The path to the tier-1 location where the data is read from.
    credit_card_balance : str
        The name of the credit card balance file.
    tier2_loc : str
        The path to the tier-2 location where the transformed data is saved.
    """

    if file_check(tier1_loc,credit_card_balance):
        #Reading file
        ccb = pd.read_csv(tier1_loc+credit_card_balance)
        #Dropping prev_id as it is not needed for the join
        ccb.drop(['SK_ID_PREV'],axis =1,inplace=True)
        #One hot encoding for all categorical columns
        ccb = one_hot_encoder(ccb, nan_as_category= True)
        #Aggregating all columns based on SK_ID_CURR
        ccb_agg = ccb.groupby('SK_ID_CURR').agg(['min','max','mean','var'])
        #Cleaning column names after aggregation
        ccb_agg.columns = pd.Index(['ccb_' + e[0] + "_" + e[1] for e in ccb_agg.columns.tolist()])
        #Getting count of credit accounts for each unique ID
        ccb_agg['cc_count'] = ccb.groupby('SK_ID_CURR').size()
        #Deleting intermediate dataframes
        del ccb
        #Removing any constant columns    
        ccb_agg = ccb_agg.loc[:, (ccb_agg != ccb_agg.iloc[0]).any()] 
        #Saving
        ccb_agg.to_csv(path_or_buf = tier2_loc+credit_card_balance,index=False)


def ip_ltw(tier1_loc,installments_payments,tier2_loc):
    """
    This function loads installments payments data from tier-1,
    applies transformations,and writes the data to tier-2.
    Parameters
    ----------
    tier1_loc : str
        The path to the tier-1 location where the data is read from.
    installments_payments : str
        The name of the installments payments file.
    tier2_loc : str
        The path to the tier-2 location where the transformed data is saved.
    """

    if file_check(tier1_loc,installments_payments):
        #Reading installments_payments.csv
        ip = pd.read_csv(tier1_loc+installments_payments)
        #Dropping prev_id as it is not needed for the join
        ip.drop(['SK_ID_PREV'],axis =1,inplace=True)
        #One hot encoding for all categorical columns
        ip = one_hot_encoder(ip, nan_as_category= True)
        #Aggregating all columns based on SK_ID_CURR
        ip_agg = ip.groupby('SK_ID_CURR').agg(['min','max','mean','var'])
        #Cleaning column names after aggregation
        ip_agg.columns = pd.Index(['ip_' + e[0] + "_" + e[1] for e in ip_agg.columns.tolist()])
        #Getting count of installment accounts for each unique ID
        ip_agg['ip_count'] = ip.groupby('SK_ID_CURR').size()
        #Deleting intermediate dataframes
        del ip
        #Removing any constant columns    
        ip_agg = ip_agg.loc[:, (ip_agg != ip_agg.iloc[0]).any()] 
        #Saving
        ip_agg.to_csv(path_or_buf = tier2_loc+installments_payments,index=False)


def pcb_ltw(tier1_loc,pos_cash_balance,tier2_loc):
    """
    This function loads pos cash balance data from tier-1,
    applies transformations,and writes the data to tier-2.
    Parameters
    ----------
    tier1_loc : str
        The path to the tier-1 location where the data is read from.
    pos_cash_balance : str
        The name of the pos cash balance file.
    tier2_loc : str
        The path to the tier-2 location where the transformed data is saved.
    """
    
    if file_check(tier1_loc,pos_cash_balance):
        #Reading pos_cash_balance.csv
        pcb = pd.read_csv(tier1_loc+pos_cash_balance)    
        #Dropping prev_id as it is not needed for the join
        pcb.drop(['SK_ID_PREV'],axis =1,inplace=True)    
        #One hot encoding for all categorical columns
        pcb = one_hot_encoder(pcb, nan_as_category= True)    
        #Aggregating all columns based on SK_ID_CURR
        pcb_agg = pcb.groupby('SK_ID_CURR').agg(['min','max','mean','var'])    
        #Cleaning column names after aggregation
        pcb_agg.columns = pd.Index(['ip_' + e[0] + "_" + e[1] for e in pcb_agg.columns.tolist()])    
        #Getting count of installment accounts for each unique ID
        pcb_agg['pcb_count'] = pcb.groupby('SK_ID_CURR').size()
        #Deleting intermediate dataframes
        del pcb
        #Removing any constant columns    
        pcb_agg = pcb_agg.loc[:, (pcb_agg != pcb_agg.iloc[0]).any()] 
        #Saving
        pcb_agg.to_csv(path_or_buf = tier2_loc+pos_cash_balance,index=False)

def main():
    # Checking if the tier-1 directory is present in the project directory
    if not os.path.isdir(tier1_loc):
        print("Tier-1 folder is missing in project dir, please create and re-run")
        #raise NotADirectoryError("tier-1 folder is missing in project dir.")
        sys.exit()

    #Checking if tier-2 exists, if not, then creating        
    if not os.path.isdir(tier2_loc):
        print("Creating tier-2 folder")
        os.mkdir(tier2_loc)
        
    train_test_ltw(tier1_loc,train,test,tier2_loc)
    previous_application_ltw(tier1_loc,previous_application,tier2_loc)
    bureau_ltw(tier1_loc,bureau,tier2_loc)
    bureau_balance_ltw(tier1_loc,bureau_balance,tier2_loc)
    ccb_ltw(tier1_loc,credit_card_balance,tier2_loc)
    ip_ltw(tier1_loc,installments_payments,tier2_loc)
    pcb_ltw(tier1_loc,pos_cash_balance,tier2_loc)
    

if __name__ == "__main__":
    main()
    



