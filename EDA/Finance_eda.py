import pandas as pd
import numpy as np

df=pd.read_csv("Data_Cleaning/Finance_cleaned.csv")

#####univariate

#Income
df["Income"].mean()
df["Income"].median()
df["Income"].mode()
df["Income"].std()
df["Income"].min()
df["Income"].max()

#Food
df["Food"].mean()
df["Food"].median()
df["Food"].mode()
df["Food"].std()
df["Food"].min()
df["Food"].max()

#Shopping
df["Shopping"].mean()
df["Shopping"].median()
df["Shopping"].mode()
df["Shopping"].std()
df["Shopping"].min()
df["Shopping"].max()

#Transport
df["Transport"].mean()
df["Transport"].median()
df["Transport"].mode()
df["Transport"].std()
df["Transport"].min()
df["Transport"].max()

#Entertainment
df["Entertainment"].mean()
df["Entertainment"].median()
df["Entertainment"].mode()
df["Entertainment"].std()
df["Entertainment"].min()
df["Entertainment"].max()

#Bill_Paid
df["Bill_Paid"].mean()
df["Bill_Paid"].median()
df["Bill_Paid"].mode()
df["Bill_Paid"].std()
df["Bill_Paid"].min()
df["Bill_Paid"].max()

#Savings
df["Savings"].mean()
df["Savings"].median()
df["Savings"].mode()
df["Savings"].std()
df["Savings"].min()
df["Savings"].max()

#######handling outliers
#Income
Q1=df["Income"].quantile(0.25)
Q3=df["Income"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Income_outliers=df[(df["Income"]<lower_bound) | (df["Income"]>upper_bound)]

#Food
Q1=df["Food"].quantile(0.25)
Q3=df["Food"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Food_outliers=df[(df["Food"]<lower_bound) | (df["Food"]>upper_bound)]

#Shopping
Q1=df["Shopping"].quantile(0.25)
Q3=df["Shopping"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Shopping_outliers=df[(df["Shopping"]<lower_bound) | (df["Shopping"]>upper_bound)]

#Transport
Q1=df["Transport"].quantile(0.25)
Q3=df["Transport"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Transport_outliers=df[(df["Transport"]<lower_bound) | (df["Transport"]>upper_bound)]

#Entertainment
Q1=df["Entertainment"].quantile(0.25)
Q3=df["Entertainment"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Entertainment_outliers=df[(df["Entertainment"]<lower_bound) | (df["Entertainment"]>upper_bound)]

#Bill_Paid
Q1=df["Bill_Paid"].quantile(0.25)
Q3=df["Bill_Paid"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Bill_Paid_outliers=df[(df["Bill_Paid"]<lower_bound) | (df["Bill_Paid"]>upper_bound)]

#Savings
Q1=df["Savings"].quantile(0.25)
Q3=df["Savings"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Savings_outliers=df[(df["Savings"]<lower_bound) | (df["Savings"]>upper_bound)]
print(Savings_outliers)
print(Bill_Paid_outliers)


######correlation analysis
columns=["Income",
         "Food",
         "Shopping",
         "Transport",
         "Entertainment",
         "Bill_Paid",
         "Savings"
         ]
corr_data=df[columns]
corr_matrix=corr_data.corr()