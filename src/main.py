import auto_ft
import tier2_load
import tier3_load
import model_builder
import os
import argparse


def main():
    """ Main function
    """

    cwd = os.getcwd()

    parser = argparse.ArgumentParser(
        description=('Generates features, trains the model, \
                     and outputs predictions.'),
        add_help='How to use', prog='main.py <args>')

    parser.add_argument(
        "-d",
        "--data_path",
        default=cwd,
        help=("Provide the path to the parent directory containing \
              tier-1 folder"))

    parser.add_argument(
        "-m",
        "--mode",
        default='all',
        choices=[
            'all',
            'features',
            'model'],
        help=("Whether to create features or train the model or both"))

    parser.add_argument(
        "-ft",
        "--feature_type",
        default='auto',
        choices=[
            'auto',
            'manual'],
        help=("Whether to create features using manual feature extraction \
              or auto feature extraction "))

    parser.add_argument("-p", "--primitive_set", default='some',
                        choices=['some', 'all'],
                        help=("Choose the primitive set."))

    parser.add_argument("-i", "--imp_thresh", default=0,
                        help=("Provide the threshold for feature selection."))

    args = parser.parse_args()

    # Names of all tier-1 csv files
    credit_card_balance = "credit_card_balance.csv"
    installments_payments = "installments_payments.csv"
    pos_cash_balance = "POS_CASH_balance.csv"
    bureau = "bureau.csv"
    bureau_balance = "bureau_balance.csv"
    previous_application = "previous_application.csv"
    train = "application_train.csv"
    test = "application_test.csv"

    submission_file_name = "sub_gbm.csv"

    # Directory of folder location
    path = args.data_path
    tier1_loc = path + "/tier1/"
    tier2_loc = path + "/tier2/"
    tier3_loc = path + "/tier3/"

    # Name of file to write into tier-3
    if args.feature_type == 'auto':
        train_write = "train_auto.csv"
        test_write = "test_auto.csv"
    else:
        train_write = "train_manual.csv"
        test_write = "test_manual.csv"

    if args.mode == 'all':

        if args.feature_type == 'auto':
            # Calling auto feature matrix generation
            auto_ft.load_feature_matrix(
                tier1_loc, args.primitive_set, float(
                    args.imp_thresh), tier3_loc, train_write, test_write)

        if args.feature_type == 'manual':
            # Running tier-2 load script
            tier2_load.tier2_loader(
                tier1_loc,
                tier2_loc,
                train,
                test,
                previous_application,
                bureau,
                bureau_balance,
                credit_card_balance,
                installments_payments,
                pos_cash_balance)
            # Running tier-3 load script
            tier3_load.tier3_loader(
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
                pos_cash_balance)

        # Training on features
        model_builder.model_train(
            path,
            tier3_loc,
            train_write,
            test_write,
            submission_file_name)

    if args.mode == 'features':

        if args.feature_type == 'auto':
            # Calling auto feature matrix generation
            auto_ft.load_feature_matrix(
                tier1_loc, args.primitive_set, float(
                    args.imp_thresh), tier3_loc, train_write, test_write)

        if args.feature_type == 'manual':
            # Running tier-2 load script
            tier2_load.tier2_loader(
                tier1_loc,
                tier2_loc,
                train,
                test,
                previous_application,
                bureau,
                bureau_balance,
                credit_card_balance,
                installments_payments,
                pos_cash_balance)
            # Running tier-3 load script
            tier3_load.tier3_loader(
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
                pos_cash_balance)

    if args.mode == 'model':

        # Training on features
        model_builder.model_train(
            path,
            tier3_loc,
            train_write,
            test_write,
            submission_file_name)


if __name__ == "__main__":
    main()
