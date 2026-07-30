import pandas as pd

df=pd.read_csv("../Data_Cleaning/Productivity_cleaned.csv")

#Create date-based features
df["Date"]=pd.to_datetime(df["Date"])
df["Day"]=df["Date"].dt.day
df["Month"]=df["Date"].dt.month
df["Year"]=df["Date"].dt.year
df["Day_Name"]=df["Date"].dt.day_name()
df["Weekday"]=df["Date"].dt.weekday




#Create Total Productive Hours
df["Total_Productive_Hours"]=(
    df["Study_Hours"]+
    df["Coding_Hours"]+
    (df["Reading_Minutes"]/60)+
    (df["Exercise_Minutes"]/60)
).round(2)

#Create Total Distraction Hours
df["Total_Distraction_Hours"]=df["Screen_Time"]

#Productivity Ratio
df["Productivity_Ratio"]=(df["Total_Productive_Hours"]/(df["Total_Productive_Hours"]+df["Total_Distraction_Hours"])).round(2)

#Productive Day
df["Productive_Day"]=(
    df["Total_Productive_Hours"]>=6
).astype(int)

df.to_csv(
    "../Feature_Engineering/Productivity_Feature_Engineering.csv",
    index=False
)

print(df)