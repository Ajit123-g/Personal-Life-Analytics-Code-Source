import pandas as pd

df=pd.read_csv("Data_Cleaning/Health_cleaned.csv")

#Create Sleep Category
df["Sleep_Category"]=pd.cut(df["Sleep_Hours"], bins=[0, 5, 7, 9, 24], labels=[" VeryPoor", "Poor", "Good", "Oversleep"])

#Create Water Intake Category
df["Water_Category"]=pd.cut(
    df["Water_Intake"],
    bins=[0, 3, 6, 10],
    labels=["Low", "Normal", "High"]
)

#Create Activity Level from Steps
df["Activity_Level"]=pd.cut(
    df["Steps"],
    bins=[0, 5000, 10000, 100000],
    labels=["Low", "Moderate", "High"]
)

#Create Health Day
df["Healthy_Day"]=(
    (df["Sleep_Hours"]>=7) &
    (df["Water_Intake"]>=3) &
    (df["Steps"]>=5000)
)

df.to_csv(
    "Feature_Engineering/Health_Feature_Engineering.csv",
    index=False
)

print(df)