import pandas as pd
import numpy as np

df=pd.read_csv("../Data_Cleaning/Health_cleaned.csv")

######univariate analysis

#for mean
Sleep_Hours_mean=df["Sleep_Hours"].mean()
Water_Intake_mean=df["Water_Intake"].mean()
Steps_mean=df["Steps"].mean()
Weight_mean=df["Weight"].mean()
Calories_mean=df["Calories"].mean()


#for median
Sleep_Hours_median=df["Sleep_Hours"].median()
Water_Intake_median=df["Water_Intake"].median()
Steps_median=df["Steps"].median()
Weight_median=df["Weight"].median()
Calories_median=df["Calories"].median()


#for  minimum
Sleep_Hours_minimum=df["Sleep_Hours"].min()
Water_Intake_minimum=df["Water_Intake"].min()
Steps_minimum=df["Steps"].min()
Weight_minimum=df["Weight"].min()
Calories_minimum=df["Calories"].min()

#for maximum
Sleep_Hours_maximum=df["Sleep_Hours"].max()
Water_Intake_maximum=df["Water_Intake"].max()
Steps_maximum=df["Steps"].max()
Weight_maximum=df["Weight"].max()
Calories_maximum=df["Calories"].max()



#for standard_deviation
Sleep_Hours_standard_deviation=df["Sleep_Hours"].std()
Water_Intake_standard_deviation=df["Water_Intake"].std()
Steps_standard_deviation=df["Steps"].std()
Weight_standard_deviation=df["Weight"].std()
Calories_standard_deviation=df["Calories"].std()

#for distribution
#for outliers
#Sleep_Hours
Q1=df["Sleep_Hours"].quantile(0.25)
Q3=df["Sleep_Hours"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Study_Hours_outliers=df[(df["Sleep_Hours"]<lower_bound) | (df["Sleep_Hours"]>upper_bound)]

#Water_Intake
Q1=df["Water_Intake"].quantile(0.25)
Q3=df["Water_Intake"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Coding_Hours_outliers=df[(df["Water_Intake"]<lower_bound) | (df["Water_Intake"]>upper_bound)]

#Steps
Q1=df["Steps"].quantile(0.25)
Q3=df["Steps"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Exercise_Minutes_outliers=df[(df["Steps"]<lower_bound) | (df["Steps"]>upper_bound)]

#Weight
Q1=df["Weight"].quantile(0.25)
Q3=df["Weight"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Reading_Minutes_outliers=df[(df["Weight"]<lower_bound) | (df["Weight"]>upper_bound)]

#Calories
Q1=df["Calories"].quantile(0.25)
Q3=df["Calories"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Screen_Time_outliers=df[(df["Calories"]<lower_bound) | (df["Calories"]>upper_bound)]

######correlation analysis
columns=["Sleep_Hours",
         "Water_Intake",
         "Steps",
         "Weight",
         "Calories"
         ]
corr_data=df[columns]
corr_matrix=corr_data.corr()

####unique value
df["Mood"].nunique()
df["Stress_Level"].nunique()

#####value_counts
df["Mood"].value_counts()
df["Stress_Level"].value_counts()

#########outliers are determine in the univariate use that

print(corr_matrix)