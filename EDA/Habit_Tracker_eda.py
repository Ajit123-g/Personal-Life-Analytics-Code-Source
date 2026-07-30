import pandas as pd
import numpy as np

df=pd.read_csv("../Data_Cleaning/Habit_cleaned.csv")


#####univariate

#Medition_Minutes
df["Medition_Minutes"].mean()
df["Medition_Minutes"].median()
df["Medition_Minutes"].mode()
df["Medition_Minutes"].std()
df["Medition_Minutes"].min()
df["Medition_Minutes"].max()

#Gym_Minutes
df["Gym_Minutes"].mean()
df["Gym_Minutes"].median()
df["Gym_Minutes"].mode()
df["Gym_Minutes"].std()
df["Gym_Minutes"].min()
df["Gym_Minutes"].max()

#Coding_Hours
df["Coding_Hours"].mean()
df["Coding_Hours"].median()
df["Coding_Hours"].mode()
df["Coding_Hours"].std()
df["Coding_Hours"].min()
df["Coding_Hours"].max()

#Reading_Minutes
df["Reading_Minutes"].mean()
df["Reading_Minutes"].median()
df["Reading_Minutes"].mode()
df["Reading_Minutes"].std()
df["Reading_Minutes"].min()
df["Reading_Minutes"].max()

#Journaling_Minutes
df["Journaling_Minutes"].mean()
df["Journaling_Minutes"].median()
df["Journaling_Minutes"].mode()
df["Journaling_Minutes"].std()
df["Journaling_Minutes"].min()
df["Journaling_Minutes"].max()



#####Total time spend
total_medition=df["Medition_Minutes"].sum()
total_gym=df["Gym_Minutes"].sum()
total_coding=df["Coding_Hours"].sum()
total_reading=df["Reading_Minutes"].sum()
total_journaling=df["Journaling_Minutes"].sum()

######correlation analysis
columns=["Medition_Minutes",
         "Gym_Minutes",
         "Coding_Hours",
         "Reading_Minutes",
         "Journaling_Minutes"
         ]
corr_data=df[columns]
corr_matrix=corr_data.corr()


#######handling outliers
#Medition_Minutes
Q1=df["Medition_Minutes"].quantile(0.25)
Q3=df["Medition_Minutes"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Medition_Minutes_outliers=df[(df["Medition_Minutes"]<lower_bound) | (df["Medition_Minutes"]>upper_bound)]

#Gym_Minutes
Q1=df["Gym_Minutes"].quantile(0.25)
Q3=df["Gym_Minutes"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Screen_Time_outliers=df[(df["Gym_Minutes"]<lower_bound) | (df["Gym_Minutes"]>upper_bound)]

#Coding_Hours
Q1=df["Coding_Hours"].quantile(0.25)
Q3=df["Coding_Hours"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Screen_Time_outliers=df[(df["Coding_Hours"]<lower_bound) | (df["Coding_Hours"]>upper_bound)]

#Reading_Minutes
Q1=df["Reading_Minutes"].quantile(0.25)
Q3=df["Reading_Minutes"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Screen_Time_outliers=df[(df["Reading_Minutes"]<lower_bound) | (df["Reading_Minutes"]>upper_bound)]

#Journaling_Minutes
Q1=df["Journaling_Minutes"].quantile(0.25)
Q3=df["Journaling_Minutes"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Screen_Time_outliers=df[(df["Journaling_Minutes"]<lower_bound) | (df["Journaling_Minutes"]>upper_bound)]