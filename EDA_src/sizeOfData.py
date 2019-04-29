# package for high-performance, easy-to-use data structures and data analysis
import pandas as pd


def assignDataToVariables():
    """
    This function assigns all the CSV files to a variable for future references
    """
    application_train = pd.read_csv('../input/application_train.csv')
    POS_CASH_balance = pd.read_csv('../input/POS_CASH_balance.csv')
    bureau_balance = pd.read_csv('../input/bureau_balance.csv')
    previous_application = pd.read_csv('../input/previous_application.csv')
    installments_payments = pd.read_csv('../input/installments_payments.csv')
    credit_card_balance = pd.read_csv('../input/credit_card_balance.csv')
    bureau = pd.read_csv('../input/bureau.csv')
    application_test = pd.read_csv('../input/application_test.csv')


def sizeOfDataSets():
    """
    This function is used to check the size of all the CSV files
    i.e The number of rows and coloumns in each CSV file
    """
    print('Size of application_train data', application_train.shape)
    print('Size of POS_CASH_balance data', POS_CASH_balance.shape)
    print('Size of bureau_balance data', bureau_balance.shape)
    print('Size of previous_application data', previous_application.shape)
    print(
        'Size of installments_payments data',
        installments_payments.shape)
    print('Size of credit_card_balance data', credit_card_balance.shape)
    print('Size of bureau data', bureau.shape)
