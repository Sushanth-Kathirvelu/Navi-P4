import sizeOfData


def missingValues():
    """
    This function is used to find the number of missing values in the CSV file
    in each Coloumns and the percentage of missing data in that particular
    coloumn
    """
    sizeOfData.assignDataToVariables()

    # checking missing data in applicaion_train CSV file
    total = application_train.isnull().sum().sort_values(ascending=False)
    percent = (
        application_train.isnull().sum() /
        application_train.isnull().count() *
        100).sort_values(
        ascending=False)
    missing_application_train_data = pd.concat(
        [total, percent], axis=1, keys=['Total', 'Percent'])
    missing_application_train_data.head(20)

    # checking missing data in POS_CASH_balance .CSV file
    total = POS_CASH_balance.isnull().sum().sort_values(ascending=False)
    percent = (
        POS_CASH_balance.isnull().sum() /
        POS_CASH_balance.isnull().count() *
        100).sort_values(
        ascending=False)
    missing_POS_CASH_balance_data = pd.concat(
        [total, percent], axis=1, keys=['Total', 'Percent'])
    missing_POS_CASH_balance_data.head(3)

    # checking missing data in bureau_ balance .CSV file
    total = bureau_balance.isnull().sum().sort_values(ascending=False)
    percent = (
        bureau_balance.isnull().sum() /
        bureau_balance.isnull().count() *
        100).sort_values(
        ascending=False)
    missing_bureau_balance_data = pd.concat(
        [total, percent], axis=1, keys=['Total', 'Percent'])
    missing_bureau_balance_data.head(3)

    # checking missing data in previous_application .CSV file
    total = previous_application.isnull().sum().sort_values(ascending=False)
    percent = (
        previous_application.isnull().sum() /
        previous_application.isnull().count() *
        100).sort_values(
        ascending=False)
    missing_previous_application_data = pd.concat(
        [total, percent], axis=1, keys=['Total', 'Percent'])
    missing_previous_application_data.head(15)

    # checking missing data in installments_payments .CSV file
    total = installments_payments.isnull().sum().sort_values(ascending=False)
    percent = (
        installments_payments.isnull().sum() /
        installments_payments.isnull().count() *
        100).sort_values(
        ascending=False)
    missing_installments_payments_data = pd.concat(
        [total, percent], axis=1, keys=['Total', 'Percent'])
    missing_installments_payments_data.head(3)

    # checking missing data in credit_card_balance .CSV file
    total = credit_card_balance.isnull().sum().sort_values(ascending=False)
    percent = (
        credit_card_balance.isnull().sum() /
        credit_card_balance.isnull().count() *
        100).sort_values(
        ascending=False)
    missing_credit_card_balance_data = pd.concat(
        [total, percent], axis=1, keys=['Total', 'Percent'])
    missing_credit_card_balance_data.head(10)

    # checking missing data in bureau .CSV file
    total = bureau.isnull().sum().sort_values(ascending=False)
    percent = (
        bureau.isnull().sum() /
        bureau.isnull().count() *
        100).sort_values(
        ascending=False)
    missing_bureau_data = pd.concat(
        [total, percent], axis=1, keys=['Total', 'Percent'])
    missing_bureau_data.head(8)
