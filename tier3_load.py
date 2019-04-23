#Script reads all files from tier-2,joins them based on keys, and saves to tier-3

#import argparse
import pandas as pd
#import os

dir = "/Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4"
tier2_loc = dir+"/tier2/"
tier3_loc = dir+"/tier3/"

credit_card_balance = "credit_card_balance.csv"
installments_payments = "installments_payments.csv"
pos_cash_balance = "POS_CASH_balance.csv"
bureau = "bureau.csv"
bureau_balance = "bureau_balance.csv"
previous_application = "previous_application.csv"
train = "application_train.csv"
test = "application_test.csv"

#Reading train dataset
train_df = pd.read_csv(tier2_loc+train)

#Reading test dataset
test_df = pd.read_csv(tier2_loc+test)

#Reading previous_application.csv
pa = pd.read_csv(tier2_loc+previous_application)

#Reading bureau.csv
b = pd.read_csv(tier2_loc+bureau)

#Reading bureau_balance.csv
bb = pd.read_csv(tier2_loc+bureau_balance)

#Reading credit_card_balance.csv
ccb = pd.read_csv(tier2_loc+credit_card_balance)

#Reading installments_payments.csv
ip = pd.read_csv(tier2_loc+installments_payments)

#Reading pos_cash_balance.csv
pcb = pd.read_csv(tier2_loc+pos_cash_balance)

#Joining bureau_balance(aggregated) and bureau
b.shape
bureau_df = b.join(bb, how='left', on='SK_ID_BUREAU')
bureau_df.drop(['SK_ID_BUREAU'],axis =1,inplace=True)
bureau_df.shape


def perform_joins(df):
    df = df.join(bureau_df, how='left', on='SK_ID_CURR',rsuffix='bb')
    df = df.join(pa, how='left', on='SK_ID_CURR',rsuffix='pa')
    df = df.join(pcb, how='left', on='SK_ID_CURR',rsuffix='pcb')
    df = df.join(ip, how='left', on='SK_ID_CURR',rsuffix='ip')
    df = df.join(ccb, how='left', on='SK_ID_CURR',rsuffix='ccb')
    return df


train_df.shape
train_set = perform_joins(train_df)
train_set.shape

test_df.shape
test_set = perform_joins(test_df)
test_set.shape

train_set.to_csv(path_or_buf = tier3_loc+train,index=False)
test_set.to_csv(path_or_buf = tier3_loc+test,index=False)
