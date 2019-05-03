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

## Running
  
## References

* https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction
* https://www.kaggle.com/codename007/home-credit-complete-eda-feature-importance
* https://docs.featuretools.com/index.html

## Ethics Considerations
This project could be used as a part of a study on the loan repayment abilities for an individual. With this context in mind, we have undertaken certain ethics considerations to ensure that this project cannot be misused for purposes other than the ones intended.

See the [ETHICS.md](https://github.com/dsp-uga/Navi-P4/blob/master/ETHICS.md) file for details.
Also see the [Wiki Ethics page](https://github.com/dsp-uga/Navi-P4/wiki/Ethics) for explanations about the ethics considerations.

## Contibutors
See the contributors file for details. 

[Contributors](https://github.com/dsp-uga/Navi-P4/blob/master/Contributors.md)

## License
This project is licensed under the MIT License- see the [LICENSE.md]( https://github.com/dsp-uga/Navi-P4/blob/master/LICENSE) file for details

