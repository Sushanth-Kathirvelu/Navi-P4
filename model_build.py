#Script reads train and test files from tier-3 and implements ML techniques on them

#import argparse
import pandas as pd
#import os

dir = "/Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4"
tier3_loc = dir+"/tier3/"

train = "application_train.csv"
test = "application_test.csv"

#Reading train dataset
train_df = pd.read_csv(tier3_loc+train)

#Reading test dataset
test_df = pd.read_csv(tier3_loc+test)
