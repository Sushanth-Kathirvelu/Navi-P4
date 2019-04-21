#Script reads all files from tier-1, applies required transformations, joins them based on keys, and saves to tier-2
#import argparse
import pandas as pd
#import os
import gc
import copy

tier1_loc = "/Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4/tier1/"
credit_card_balance = "credit_card_balance.csv"
installments_payments = "installments_payments.csv"
pos_cash_balance = "POS_CASH_balance.csv"
bureau = "bureau.csv"
bureau_balance = "bureau_balance.csv"
previous_application = "previous_application.csv"
train = "application_train.csv"
test = "application_test.csv"

# One-hot encoding for categorical columns with get_dummies
def one_hot_encoder(df, nan_as_category = True):
    categorical_columns = [col for col in df.columns if df[col].dtype == 'object']
    df = pd.get_dummies(df, columns= categorical_columns, dummy_na= nan_as_category)
    return df


##############################################################################################
#Reading and pre-processing application_train.csv and test_application.csv
##############################################################################################

#Reading train dataset
train_df = pd.read_csv(tier1_loc+train)

train_df.count()
#train has 307,511

#Reading test dataset
test_df = pd.read_csv(tier1_loc+test)
test_df.count()

#Length of training set
train_objs_num = len(train_df)

#Joining train and test to perform tranformations
dataset = pd.concat(objs=[train_df, test_df], axis=0)
dataset = one_hot_encoder(dataset, nan_as_category= True)
train_df = copy.copy(dataset[:train_objs_num])
test_df = copy.copy(dataset[train_objs_num:])

##############################################################################################
#Reading and pre-processing previous_application.csv
##############################################################################################

#Reading previous_application.csv
pa = pd.read_csv(tier1_loc+previous_application)
pa.shape
#1670214*37

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
    
pa_agg.pa_count.describe()

del pa
gc.collect()

##############################################################################################
#Reading and pre-processing bureau.csv
##############################################################################################

#Reading bureau.csv
b = pd.read_csv(tier1_loc+bureau)

#One hot encoding for all categorical columns
b = one_hot_encoder(b, nan_as_category= True)

##############################################################################################
#Reading and pre-processing bureau_balance.csv
##############################################################################################

bb = pd.read_csv(tier1_loc+bureau_balance)

#One hot encoding for all categorical columns
bb = one_hot_encoder(bb, nan_as_category= True)

#Aggregating all columns based on SK_ID_CURR
bb_agg = bb.groupby('SK_ID_BUREAU').agg(['min','max','mean','var'])

#Cleaning column names after aggregation
bb_agg.columns = pd.Index(['bb_' + e[0] + "_" + e[1] for e in bb_agg.columns.tolist()])

#Getting count of credit accounts for each unique ID
bb_agg['bb_count'] = bb.groupby('SK_ID_BUREAU').size()
    
bb_agg.bb_count.describe()

del bb

##############################################################################################
#Reading and pre-processing credit_card_balance.csv
##############################################################################################

#Reading file
ccb = pd.read_csv(tier1_loc+credit_card_balance)
ccb.shape
#3,840,312*23

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
    
ccb_agg.cc_count.describe()

del ccb

##############################################################################################
#Reading and pre-processing installments_payments.csv
##############################################################################################

#Reading installments_payments.csv
ip = pd.read_csv(tier1_loc+installments_payments)
ip.shape
#13,605,401*8


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
    
ip_agg.ip_count.describe()

del ip

##############################################################################################
#Reading and pre-processing POS_CASH_balance.csv
##############################################################################################

#Reading pos_cash_balance.csv
pcb = pd.read_csv(tier1_loc+pos_cash_balance)
pcb.shape
#10,001,358*8

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
    
pcb_agg.pcb_count.describe()

del pcb

##############################################################################################




