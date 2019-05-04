import sizeOfData
import cufflinks as cf
import plotly.offline as offline
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
import plotly.offline as py
import pandas as pd
# package for high-performance, easy-to-use data structures and data analysis
import numpy as np  # fundamental package for scientific computing with Python
import matplotlib
import matplotlib.pyplot as plt  # for plotting
import seaborn as sns  # for making plots with seaborn
color = sns.color_palette()
py.init_notebook_mode(connected=True)
init_notebook_mode(connected=True)
offline.init_notebook_mode()
# from plotly import tools
# import plotly.tools as tls
# import squarify
# from mpl_toolkits.basemap import Basemap
# from numpy import array
# from matplotlib import cm

# import cufflinks and offline mode
cf.go_offline()

# from sklearn import preprocessing
# # Supress unnecessary warnings so that presentation looks clean
# import warnings
# warnings.filterwarnings("ignore")

# # Print all rows and columns
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


sizeOfData.assignDataToVariables()


def incomeSourceVSLoan():
    temp = application_train["NAME_INCOME_TYPE"].value_counts()
    # print(temp.values)
    temp_y0 = []
    temp_y1 = []
    for val in temp.index:
        first = (np.sum(
            application_train["TARGET"][application_train["NAME_INCOME_TYPE"] == val] == 1))
        second = (np.sum(
            application_train["TARGET"][application_train["NAME_INCOME_TYPE"] == val] == 0))
        total = first + second
        first = first / total * 100
        second = second / total * 100
        temp_y1.append(first)
        temp_y0.append(second)
    trace1 = go.Bar(
        x=temp.index,
        y=temp_y1,
        #y = (temp_y1 / temp.sum()) * 100,
        name='NO'
    )
    trace2 = go.Bar(
        x=temp.index,
        y=temp_y0,
        #y = (temp_y0 / temp.sum()) * 100,
        name='YES'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="Income sources of Applicant's in terms of loan is repayed or not  in %",
        # barmode='stack',
        width=1000,
        xaxis=dict(
            title='Income source',
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count in %',
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
    iplot(fig)


def familyStatusVSLoan():
    temp = application_train["NAME_FAMILY_STATUS"].value_counts()
    # print(temp.values)
    temp_y0 = []
    temp_y1 = []
    for val in temp.index:
        first = (np.sum(
            application_train["TARGET"][application_train["NAME_FAMILY_STATUS"] == val] == 1))
        second = (np.sum(
            application_train["TARGET"][application_train["NAME_FAMILY_STATUS"] == val] == 0))
        total = first + second
        first = first / total * 100
        second = second / total * 100
        temp_y1.append(first)
        temp_y0.append(second)
    trace1 = go.Bar(
        x=temp.index,
        y=temp_y1,
        #y = (temp_y1 / temp.sum()) * 100,
        name='NO'
    )
    trace2 = go.Bar(
        x=temp.index,
        #y = (temp_y0 / temp.sum()) * 100,
        y=temp_y0,
        name='YES'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="Family Status of Applicant's in terms of loan is repayed or not in %",
        # barmode='stack',
        width=1000,
        xaxis=dict(
            title='Family Status',
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count in %',
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
    iplot(fig)


def occupationVSLoan():
    temp = application_train["OCCUPATION_TYPE"].value_counts()
    # print(temp.values)
    temp_y0 = []
    temp_y1 = []
    for val in temp.index:
        first = (np.sum(
            application_train["TARGET"][application_train["OCCUPATION_TYPE"] == val] == 1))
        second = (np.sum(
            application_train["TARGET"][application_train["OCCUPATION_TYPE"] == val] == 0))
        total = first + second
        first = first / total * 100
        second = second / total * 100
        temp_y1.append(first)
        temp_y0.append(second)
    trace1 = go.Bar(
        x=temp.index,
        y=temp_y1,
        #y = (temp_y1 / temp.sum()) * 100,
        name='NO'
    )
    trace2 = go.Bar(
        x=temp.index,
        #y = (temp_y0 / temp.sum()) * 100,
        y=temp_y0,
        name='YES'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="Occupation of Applicant's in terms of loan is repayed or not in %",
        # barmode='stack',
        width=1000,
        xaxis=dict(
            title='Occupation of Applicant\'s',
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count in %',
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
    iplot(fig)


def educationVSLoan():
    temp = application_train["NAME_EDUCATION_TYPE"].value_counts()
    # print(temp.values)
    temp_y0 = []
    temp_y1 = []
    for val in temp.index:
        first = np.sum(
            application_train["TARGET"][application_train["NAME_EDUCATION_TYPE"] == val] == 1)
        second = np.sum(
            application_train["TARGET"][application_train["NAME_EDUCATION_TYPE"] == val] == 0)
        total = first + second
        first = first / total * 100
        second = second / total * 100
        temp_y1.append(first)
        temp_y0.append(second)

    trace1 = go.Bar(
        x=temp.index,
        y=temp_y1,
        #y = (temp_y1 / temp.sum()) * 100,
        name='NO'
    )
    trace2 = go.Bar(
        x=temp.index,
        y=temp_y0,
        #y = (temp_y0 / temp.sum()) * 100,
        name='YES'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="Education of Applicant's in terms of loan is repayed or not in %",
        # barmode='stack',
        width=1000,
        xaxis=dict(
            title='Education of Applicant\'s',
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count in %',
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
    iplot(fig)


def typeOfHouseVSLoan():
    temp = application_train["NAME_HOUSING_TYPE"].value_counts()
    # print(temp.values)
    temp_y0 = []
    temp_y1 = []
    for val in temp.index:
        first = np.sum(
            application_train["TARGET"][application_train["NAME_HOUSING_TYPE"] == val] == 1)
        second = np.sum(
            application_train["TARGET"][application_train["NAME_HOUSING_TYPE"] == val] == 0)
        total = first + second
        first = first / total * 100
        second = second / total * 100
        temp_y1.append(first)
        temp_y0.append(second)

    trace1 = go.Bar(
        x=temp.index,
        y=temp_y1,
        #y = (temp_y1 / temp.sum()) * 100,
        name='NO'
    )
    trace2 = go.Bar(
        x=temp.index,
        y=temp_y0,
        #y = (temp_y0 / temp.sum()) * 100,
        name='YES'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="For which types of house higher applicant's applied for loan in terms of loan is repayed or not in %",
        # barmode='stack',
        width=1000,
        xaxis=dict(
            title='types of house',
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count in %',
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
    iplot(fig)


def organizationVSLoan():
    temp = application_train["ORGANIZATION_TYPE"].value_counts()
    # print(temp.values)
    temp_y0 = []
    temp_y1 = []
    for val in temp.index:
        first = np.sum(
            application_train["TARGET"][application_train["ORGANIZATION_TYPE"] == val] == 1)
        second = np.sum(
            application_train["TARGET"][application_train["ORGANIZATION_TYPE"] == val] == 0)
        total = first + second
        first = first / total * 100
        second = second / total * 100
        temp_y1.append(first)
        temp_y0.append(second)

    trace1 = go.Bar(
        x=temp.index,
        y=temp_y1,
        #y = (temp_y1 / temp.sum()) * 100,
        name='NO'
    )
    trace2 = go.Bar(
        x=temp.index,
        y=temp_y0,
        #y = (temp_y0 / temp.sum()) * 100,
        name='YES'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="Types of Organizations in terms of loan is repayed or not in %",
        # barmode='stack',
        width=1000,
        xaxis=dict(
            title='Types of Organizations',
            tickfont=dict(
                size=10,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count in %',
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
    iplot(fig)


def typeOfSuiteVSLoan():
    temp = application_train["NAME_TYPE_SUITE"].value_counts()
    # print(temp.values)
    temp_y0 = []
    temp_y1 = []
    for val in temp.index:
        first = np.sum(
            application_train["TARGET"][application_train["NAME_TYPE_SUITE"] == val] == 1)
        second = np.sum(
            application_train["TARGET"][application_train["NAME_TYPE_SUITE"] == val] == 0)
        total = first + second
        first = first / total * 100
        second = second / total * 100
        temp_y1.append(first)
        temp_y0.append(second)

    trace1 = go.Bar(
        x=temp.index,
        y=temp_y1,
        #y = (temp_y1 / temp.sum()) * 100,
        name='NO'
    )
    trace2 = go.Bar(
        x=temp.index,
        y=temp_y0,
        #y = (temp_y0 / temp.sum()) * 100,
        name='YES'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="Distribution of people accompanied in terms of loan is repayed or not in %",
        # barmode='stack',
        width=1000,
        xaxis=dict(
            title='Accompanied By',
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count in %',
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
    iplot(fig)


def ageVSLoan():
    age_data = application_train[['TARGET', 'DAYS_BIRTH']]
    age_data['YEARS_BIRTH'] = (age_data['DAYS_BIRTH'] * -1) / 365
    age_data['YEARS_BINNED'] = pd.cut(
        age_data['YEARS_BIRTH'], bins=np.linspace(
            20, 70, num=11)).astype(str)
    age_data.head
    sorted(list(temp.index))
    temp = age_data["YEARS_BINNED"].value_counts()
    # print(temp.values)
    temp_y0 = []
    temp_y1 = []
    for val in sorted(temp.index):
        first = np.sum(age_data["TARGET"]
                       [age_data["YEARS_BINNED"] == val] == 1)
        second = np.sum(age_data["TARGET"]
                        [age_data["YEARS_BINNED"] == val] == 0)
        total = first + second
        first = first / total * 100
        second = second / total * 100
        temp_y1.append(first)
        temp_y0.append(second)

    trace1 = go.Bar(
        x=sorted(temp.index),
        y=temp_y1,
        #y = (temp_y1 / temp.sum()) * 100,
        name='NO'
    )
    trace2 = go.Bar(
        x=sorted(temp.index),
        y=temp_y0,
        #y = (temp_y0 / temp.sum()) * 100,
        name='YES'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="Distribution of peoples age in terms of loan is repayed or not in %",
        # barmode='stack',
        width=1000,
        xaxis=dict(
            title='Age Group',
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Count in %',
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
    iplot(fig)
