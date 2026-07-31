import pandas as pd
import numpy as np

df=pd.read_csv("Data_Cleaning/Productivity_cleaned.csv")


######univariate analysis

#for mean
Study_Hours_mean=df["Study_Hours"].mean()
Coding_Hours_mean=df["Coding_Hours"].mean()
Exercise_Minutes_mean=df["Exercise_Minutes"].mean()
Reading_Minutes_mean=df["Reading_Minutes"].mean()
Screen_Time_mean=df["Screen_Time"].mean()
Social_Media_Time_mean=df["Social_Media_Time"].mean()
Focus_Score_mean=df["Focus_Score"].mean()




#for median
Study_Hours_median=df["Study_Hours"].median()
Coding_Hours_median=df["Coding_Hours"].median()
Exercise_Minutes_median=df["Exercise_Minutes"].median()
Reading_Minutes_median=df["Reading_Minutes"].median()
Screen_Time_median=df["Screen_Time"].median()
Social_Media_Time_median=df["Social_Media_Time"].median()
Focus_Score_median=df["Focus_Score"].median()


#for  minimum
Study_Hours_minimum=df["Study_Hours"].min()
Coding_Hours_minimum=df["Coding_Hours"].min()
Exercise_Minutes_minimum=df["Exercise_Minutes"].min()
Reading_Minutes_minimum=df["Reading_Minutes"].min()
Screen_Time_minimum=df["Screen_Time"].min()
Social_Media_Time_minimum=df["Social_Media_Time"].min()
Focus_Score_minimum=df["Focus_Score"].min()

#for maximum
Study_Hours_maximum=df["Study_Hours"].max()
Coding_Hours_maximum=df["Coding_Hours"].max()
Exercise_Minutes_maximum=df["Exercise_Minutes"].max()
Reading_Minutes_maximum=df["Reading_Minutes"].max()
Screen_Time_maximum=df["Screen_Time"].max()
Social_Media_Time_maximum=df["Social_Media_Time"].max()
Focus_Score_maximum=df["Focus_Score"].max()



#for standard_deviation
Study_Hours_standard_deviation=df["Study_Hours"].std()
Coding_Hours_standard_deviation=df["Coding_Hours"].std()
Exercise_Minutes_standard_deviation=df["Exercise_Minutes"].std()
Reading_Minutes_standard_deviation=df["Reading_Minutes"].std()
Screen_Time_standard_deviation=df["Screen_Time"].std()
Social_Media_standard_deviation=df["Social_Media_Time"].std()
Focus_Score_standard_deviation=df["Focus_Score"].std()



#for distribution
#for outliers
#Study_Hours
Q1=df["Study_Hours"].quantile(0.25)
Q3=df["Study_Hours"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Study_Hours_outliers=df[(df["Study_Hours"]<lower_bound) | (df["Study_Hours"]>upper_bound)]

#Coding_Hours
Q1=df["Coding_Hours"].quantile(0.25)
Q3=df["Coding_Hours"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Coding_Hours_outliers=df[(df["Coding_Hours"]<lower_bound) | (df["Coding_Hours"]>upper_bound)]

#Exercise_Minutes
Q1=df["Exercise_Minutes"].quantile(0.25)
Q3=df["Exercise_Minutes"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Exercise_Minutes_outliers=df[(df["Exercise_Minutes"]<lower_bound) | (df["Exercise_Minutes"]>upper_bound)]

#Reading_Minutes
Q1=df["Reading_Minutes"].quantile(0.25)
Q3=df["Reading_Minutes"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Reading_Minutes_outliers=df[(df["Reading_Minutes"]<lower_bound) | (df["Reading_Minutes"]>upper_bound)]

#Screen_Time
Q1=df["Screen_Time"].quantile(0.25)
Q3=df["Screen_Time"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Screen_Time_outliers=df[(df["Screen_Time"]<lower_bound) | (df["Screen_Time"]>upper_bound)]


#Social_Media_Time
Q1=df["Social_Media_Time"].quantile(0.25)
Q3=df["Social_Media_Time"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Social_Media_Time_outliers=df[(df["Social_Media_Time"]<lower_bound) | (df["Social_Media_Time"]>upper_bound)]
  

#Focus_Score
Q1=df["Focus_Score"].quantile(0.25)
Q3=df["Focus_Score"].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

Focus_Score_outliers=df[(df["Focus_Score"]<lower_bound) | (df["Focus_Score"]>upper_bound)]


#########Bivariate analysis
#study_hours vs focus_score
study_hours_corr=df["Study_Hours"].corr(df["Focus_Score"])


#coding_hours vs focus_score
coding_hours_corr=df["Coding_Hours"].corr(df["Focus_Score"])


#reading vs focus_score
reading_corr=df["Reading_Minutes"].corr(df["Focus_Score"])


#screen_time vs focus_score
screen_time_corr=df["Screen_Time"].corr(df["Focus_Score"])


#social_media_time vs focus_score
social_media_time_corr=df["Social_Media_Time"].corr(df["Focus_Score"])


#exercise vs focus_score
exercise_corr=df["Exercise_Minutes"].corr(df["Focus_Score"])


######correlation analysis

columns=["Study_Hours",
         "Coding_Hours",
         "Reading_Minutes",
         "Screen_Time",
         "Social_Media_Time",
         "Exercise_Minutes",
         "Focus_Score"
         ]
corr_data=df[columns]
corr_matrix=corr_data.corr()

##########Daily Productivity Insights

#Highest Study Day
highest_study=df.loc[df["Study_Hours"].idxmax()]
#Lowest Study Day
lowest_study=df.loc[df["Study_Hours"].idxmin()]

#Highest Coding Day
highest_coding=df.loc[df["Coding_Hours"].idxmax()]
#Lowest Coding Day
lowest_coding=df.loc[df["Coding_Hours"].idxmin()]

#Highest Exercise Day
highest_exercise=df.loc[df["Exercise_Minutes"].idxmax()]
#Lowest Exercise Day
lowest_exercise=df.loc[df["Exercise_Minutes"].idxmin()]

#Highest Reading Day
highest_reading=df.loc[df["Reading_Minutes"].idxmax()]
#Lowest Reading Day
lowest_reading=df.loc[df["Reading_Minutes"].idxmin()]

#Highest Screen Day
highest_screen=df.loc[df["Screen_Time"].idxmax()]
#Lowest Screen Day
lowest_screen=df.loc[df["Screen_Time"].idxmin()]

#Highest Social Day
highest_social=df.loc[df["Social_Media_Time"].idxmax()]
#Lowest Social Day
lowest_social=df.loc[df["Social_Media_Time"].idxmin()]

#Highest Focus Day
highest_focus=df.loc[df["Focus_Score"].idxmax()]
#Lowest Focus Day
lowest_focus=df.loc[df["Focus_Score"].idxmin()]


########Weekly Analysis 
df["Date"]=pd.to_datetime(df["Date"])
df["Weekday"]=df["Date"].dt.day_name()

study_weekday=df.groupby("Weekday")["Study_Hours"].mean()
coding_weekday=df.groupby("Weekday")["Coding_Hours"].mean()
exercise_weekday=df.groupby("Weekday")["Exercise_Minutes"].mean()
reading_weekday=df.groupby("Weekday")["Reading_Minutes"].mean()
screen_weekday=df.groupby("Weekday")["Screen_Time"].mean()
social_weekday=df.groupby("Weekday")["Social_Media_Time"].mean()
focus_weekday=df.groupby("Weekday")["Focus_Score"].mean()

#########Monthly Analysis
df["Date"]=pd.to_datetime(df["Date"])
df["Month"]=df["Date"].dt.to_period("M")

study_Monthly=df.groupby("Month")["Study_Hours"].mean()
coding_Monthly=df.groupby("Month")["Coding_Hours"].mean()
exercise_Monthly=df.groupby("Month")["Exercise_Minutes"].mean()
reading_Monthly=df.groupby("Month")["Reading_Minutes"].mean()
screen_Monthly=df.groupby("Month")["Screen_Time"].mean()
social_Monthly=df.groupby("Month")["Social_Media_Time"].mean()
focus_Monthly=df.groupby("Month")["Focus_Score"].mean()


#####outliers Detection

#in univariate analysis outliers are determine use that

