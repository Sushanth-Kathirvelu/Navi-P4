import pandas as pd # package for high-performance, easy-to-use data structures and data analysis
import numpy as np # fundamental package for scientific computing with Python
import matplotlib
import matplotlib.pyplot as plt # for plotting
import seaborn as sns # for making plots with seaborn
color = sns.color_palette()
import plotly.offline as py
py.init_notebook_mode(connected=True)
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.offline as offline
offline.init_notebook_mode()
# from plotly import tools
# import plotly.tools as tls
# import squarify
# from mpl_toolkits.basemap import Basemap
# from numpy import array
# from matplotlib import cm

# import cufflinks and offline mode
import cufflinks as cf
cf.go_offline()

# from sklearn import preprocessing
# # Supress unnecessary warnings so that presentation looks clean
# import warnings
# warnings.filterwarnings("ignore")

# # Print all rows and columns
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

import sizeOfData

sizeOfData.assignDataToVariables()
 
def distributionOfAMT_CREDIT():
    """
    This function plots a bar graph for the distribution of the AMT_CREDIT in 
    application_train .CSV data set
    """
    plt.figure(figsize=(12,5))
    plt.title("Distribution of AMT_CREDIT")
    ax = sns.distplot(application_train["AMT_CREDIT"])
    
def distributionOfAMT_INCOME_TOTAL():
    """
    This function plots a bar graph for the distribution of the AMT_INCOME_TOTAL in 
    application_train .CSV data set
    """
    plt.figure(figsize=(12,5))
    plt.title("Distribution of AMT_INCOME_TOTAL")
    ax = sns.distplot(application_train["AMT_INCOME_TOTAL"].dropna())
    
def distributionOfAMT_GOODS_PRICE():
     """
    This function plots a bar graph for the distribution of the AMT_GOODS_PRICE in 
    application_train .CSV data set
    """
    plt.figure(figsize=(12,5))
    plt.title("Distribution of AMT_GOODS_PRICE")
    ax = sns.distplot(application_train["AMT_GOODS_PRICE"].dropna())
    
def whoAccompaniedClient():
    """
    This function plots a bar graph of Who accompanied client when applying 
    for the  application
    """
    temp = application_train["NAME_TYPE_SUITE"].value_counts()
    trace = go.Bar(
        x = temp.index,
        y = (temp / temp.sum())*100,
    )
    data = [trace]
    layout = go.Layout(
        title = "Who accompanied client when applying for the  application in % ",
        xaxis=dict(
            title='Name of type of the Suite',
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count of Name of type of the Suite in %',
            titlefont=dict(
                size=16,
                color='rgb(107, 107, 107)'
            ),
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
    )
    )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='schoolStateNames')
    
def typesOfLoan():
    """
    This function plots a pi chart of the Type of loan the applicant is 
    applying for.
    """
    temp = application_train["NAME_CONTRACT_TYPE"].value_counts()
    fig = {
      "data": [
        {
          "values": temp.values,
          "labels": temp.index,
          "domain": {"x": [0, .48]},
          #"name": "Types of Loans",
          #"hoverinfo":"label+percent+name",
          "hole": .7,
          "type": "pie"
        },
        
        ],
      "layout": {
            "title":"Types of loan",
            "annotations": [
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "Loan Types",
                    "x": 0.17,
                    "y": 0.5
                }
                
            ]
        }
    }
    iplot(fig, filename='donut')
    
def purposeOfLoan():
    """
    This function plots a pi chart of the purpose of loan the applicant is 
    applying for.
    """
    temp1 = application_train["FLAG_OWN_CAR"].value_counts()
    temp2 = application_train["FLAG_OWN_REALTY"].value_counts()
    
    fig = {
      "data": [
        {
          "values": temp1.values,
          "labels": temp1.index,
          "domain": {"x": [0, .48]},
          "name": "Own Car",
          "hoverinfo":"label+percent+name",
          "hole": .6,
          "type": "pie"
        },
        {
          "values": temp2.values,
          "labels": temp2.index,
          "text":"Own Realty",
          "textposition":"inside",
          "domain": {"x": [.52, 1]},
          "name": "Own Reality",
          "hoverinfo":"label+percent+name",
          "hole": .6,
          "type": "pie"
        }],
      "layout": {
            "title":"Purpose of loan",
            "annotations": [
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "Own Car",
                    "x": 0.20,
                    "y": 0.5
                },
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "Own Realty",
                    "x": 0.8,
                    "y": 0.5
                }
            ]
        }
    }
    iplot(fig, filename='donut')
    
def incomeSources():
    """
    This function plots a pi chart for the Income sources of Applicant's
    who applied for loan
    """
    temp = application_train["NAME_INCOME_TYPE"].value_counts()
    df = pd.DataFrame({'labels': temp.index,
                       'values': temp.values
                      })
    df.iplot(kind='pie',labels='labels',values='values', title='Income sources of Applicant\'s', hole = 0.5)

def Family_Status():
    """
    This function plots a pi chart for Family Status of Applicant's
    who applied for loan
    """
    temp = application_train["NAME_FAMILY_STATUS"].value_counts()
    df = pd.DataFrame({'labels': temp.index,
                       'values': temp.values
                      })
    df.iplot(kind='pie',labels='labels',values='values', title='Family Status of Applicant\'s', hole = 0.5)
        
def occupation():
    """
    This function plots a bar chart for occupation of Applicant's
    who applied for loan
    """
    temp = application_train["OCCUPATION_TYPE"].value_counts()
    temp.iplot(kind='bar', xTitle = 'Occupation', yTitle = "Count", title = 'Occupation of Applicant\'s who applied for loan', color = 'green')    
        
def education():
    """
    This function plots a bar chart for Education of Applicant's
    who applied for loan
    """
    temp = application_train["NAME_EDUCATION_TYPE"].value_counts()
    df = pd.DataFrame({'labels': temp.index,
                       'values': temp.values
                      })
    df.iplot(kind='pie',labels='labels',values='values', title='Education of Applicant\'s', hole = 0.5)

def typeOfHouse():
    """
    This function plots a pi chart for type of house the applicant is applying
    loan for.
    """
    temp = application_train["NAME_HOUSING_TYPE"].value_counts()
    df = pd.DataFrame({'labels': temp.index,
                       'values': temp.values
                      })
    df.iplot(kind='pie',labels='labels',values='values', title='Type of House', hole = 0.5)
 
def typeOfOrganization():
    """
    This function plots a pi chart for type of Organization the applicant is applying
    loan from.
    """
    temp = application_train["ORGANIZATION_TYPE"].value_counts()
    temp.iplot(kind='bar', xTitle = 'Organization Name', yTitle = "Count", title = 'Types of Organizations who applied for loan ', color = 'red')