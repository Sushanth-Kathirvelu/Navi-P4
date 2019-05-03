# Navi-P4
## Home Credit Default Risk
Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, this population is often taken advantage of by untrustworthy lenders.

Home Credit strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience; Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.

This is a Kaggle Challenge. The link to the Challenge is as below. 

      https://www.kaggle.com/c/home-credit-default-risk/

### Goal: Predict if an applicant is capable of repaying a loan.

## Prerequisites
List of requirements and links to install them:

* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [featuretools](https://www.featuretools.com)
* [sklearn](https://scikit-learn.org/stable/)
* [lightgbm](https://lightgbm.readthedocs.io/en/latest/)
* [pandas](https://pandas.pydata.org/index.html)
* [numpy](https://www.numpy.org)

Use the setup.py to install all the Prerequisites for the Project

      python setup.py install

## Data

The Data set consist of 6 CSV files namely:

* Application_train data (307,511 * 122)
* Application_test data (48,744 * 121)
* Bureau data (1,716,428 * 17))
  * Bureau_balance data (27,299,925 * 3)       
* Previous_application data (1,670,214 * 37)
  * Installments_payments data (13,605,401 * 8)
  * Credit_card_balance data (3,840,312 * 23)
  * POS_CASH_balance data (10,001,358 * 8)              

The data are all available for download on:

      Kaggle : kaggle competitions download -c home-credit-default-risk
      
This link was provided by Kaggle .com

## Approach 
   
This project features two end-to-end approaches taken to solve the Kaggle challenge 'Home Credit Default Risk'. The first approach is using features created manually and the second approach is using an automated feature creation tool. The results of both these methods are compared and it is found that automated feature engineering can create superior features, in a shorter amount of time.

Training models: <br />
* Gradient Boosting Machines(GBM)
* RandomForest

## Directory Specifications

* Input data should follow the below structure: <br />
The project directory should contain a folder named tier1 containing all the 6 raw csv files. <br />

parent folder(project directory)  <br />
&nbsp;&nbsp;&nbsp;&nbsp;  |- tier1 <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Application_test.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Bureau.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Bureau_balance.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Previous_application.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Installments_payments.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Credit_card_balance.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--POS_CASH_balance.csv <br />

* Output once the entire code is completed will follow the below structure: <br />
The submission file is written inside the project directory. <br />

parent folder(project directory)  
&nbsp;&nbsp;&nbsp;&nbsp;  |- tier1 <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Application_test.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Bureau.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Bureau_balance.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Previous_application.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Installments_payments.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Credit_card_balance.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--POS_CASH_balance.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;  |- tier2 <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Application_test.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Bureau.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Bureau_balance.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Previous_application.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Installments_payments.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Credit_card_balance.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--POS_CASH_balance.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp; |- tier3   <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Application_train.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |--Application_test.csv <br />
&nbsp;&nbsp;&nbsp;&nbsp; |- p4sub_gbm.csv <br />


## Running the code

`main.py -d \<data_path>\ -m \<mode>\ -ft \<feature_type>\ -p \<primitive_set>\ -i \<imp_thresh>\`

**Parameters**: <br />

`<data_path>` Path to the parent folder created as per the directory specifications. <br />
Default : Current working directory. <br />

`<mode>` Mode to run the code in. <br />
Default : 'all' <br />
Choices : 'all' - To generate features and also train the model and generate predictions, <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          'features' - To only generate the features, <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          'model' - To only run the model <br />

`<feature_type>` Type of feature selection to implement <br />
Default : 'auto' <br />
Choices : 'auto' - To generate features using feature tools <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          'manual' - To generate features based on manual feature engineering <br />

`<primitive_set>` Set of primitives to consider while using feature tools
Default : 'some' <br />
Choices : 'some' - To use some of the primitives while using feature tools <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          'all' - To use all the primitives while using feature tools <br />

`<imp_thresh>` Importance threshold to consider while doing feature selection <br />
Default : '0' <br />

**Output**:

The program will output `p4sub_gbm.csv` in the given parent directory.

**Sample Run Commands and Code Flow**:

* To run the entire code using auto feature selection and gbm for model predictions: <br />

The below command will use the data from tier1, generate features using featuretools, and save the feature matrix into tier3. Then tier3 data is used to train gbm and generate predictions <br />
`python main.py -d /Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4 -m all -ft auto`

* To run the entire code using manual feature selection and gbm for model predictions: <br />

The below command will use the data from tier1, generate features using manual feature engineering techniques, and save the transformed data into tier2. Tier2 data is then joined according to the data model and saved into tier3. Then, tier3 data is used to train gbm and generate predictions. <br />
`python main.py -d /Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4 -m all -ft manual` <br />

* To generate features alone using manual/auto feature selection: <br />

The below command will use the data from tier1, generate features using manual feature engineering techniques, and save the transformed data into tier2. Tier2 data is then joined according to the data model and saved into tier3. <br />
`python main.py -d /Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4 -m features -ft manual` <br />

The below command will use the data from tier1, generate features using featuretools, and save the feature matrix into tier3. <br />
`python main.py -d /Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4 -m features -ft auto` <br />

* To train the model for features that are already generated: <br />

The below command uses features generated by auto feature selection in tier3 data to train gbm and generate predictions <br />
`python main.py -d /Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4 -m model -ft auto` <br />

The below command uses features generated by manual feature selection in tier3 data to train gbm and generate predictions <br />
`python main.py -d /Users/hemanth/Desktop/MSAI/DataSciencePracticum/Projects/p4 -m model -ft manual` <br />
  
## References

See the references Wiki page for details. 

[References Wiki](https://github.com/dsp-uga/Navi-P4/wiki/References)

## Ethics Considerations
This project could be used as a part of a study on the loan repayment abilities for an individual. With this context in mind, we have undertaken certain ethics considerations to ensure that this project cannot be misused for purposes other than the ones intended.

See the [ETHICS.md](https://github.com/dsp-uga/Navi-P4/blob/master/ETHICS.md) file for details.
Also see the [Wiki Ethics page](https://github.com/dsp-uga/Navi-P4/wiki/Ethics) for explanations about the ethics considerations.

## Contibutors
See the contributors file for details. 

[Contributors](https://github.com/dsp-uga/Navi-P4/blob/master/Contributors.md)

## License
This project is licensed under the MIT License- see the [LICENSE.md]( https://github.com/dsp-uga/Navi-P4/blob/master/LICENSE) file for details

