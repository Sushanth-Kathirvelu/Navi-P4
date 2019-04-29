import pandas as pd 
import sizeOfData

sizeOfData.assign_data_to_variables()

def data_imbalance():
    """
    This function checks for the Data Imbalance in the application_train CSV 
    and displays a graph comparing the number of persons replaying the loan vs
    the number of persons not repayig the loan
    """
    temp = application_train["TARGET"].value_counts()
    df = pd.DataFrame({'labels': temp.index,
                       'values': temp.values
                      })
    df.iplot(kind='pie',labels='labels',values='values', /
             title='Loan Repayed or not')
