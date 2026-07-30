import pandas as pd

df=pd.read_csv("../Data_Collection/Productivity.csv")

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())

df=df.drop_duplicates()


cols=["Study_Hours", "Coding_Hours", "Exercise_Minutes", "Reading_Minutes", "Screen_Time", "Social_Media_Time", "Focus_Score"]


#Convert hour columns to numbers
df["Date"]=pd.to_datetime(df["Date"])
for col in cols:
    df[col]=pd.to_numeric(df[col], errors="coerce")

    


#Handling missing values
for col in cols:
    df[col]=df[col].fillna(df[col].median())



#Detecting invalid values
mask = (df["Study_Hours"] < 0) | (df["Study_Hours"] > 24)
df.loc[mask, "Study_Hours"] = df["Study_Hours"].median()

mask = (df["Coding_Hours"] < 0) | (df["Coding_Hours"] > 24)
df.loc[mask, "Coding_Hours"] = df["Coding_Hours"].median()

mask = (df["Exercise_Minutes"] < 0) | (df["Exercise_Minutes"] > 1440)
df.loc[mask, "Exercise_Minutes"] = df["Exercise_Minutes"].median()

mask = (df["Reading_Minutes"] < 0) | (df["Reading_Minutes"] > 1440)
df.loc[mask, "Reading_Minutes"] = df["Reading_Minutes"].median()

mask = (df["Screen_Time"] < 0) | (df["Screen_Time"] > 24)
df.loc[mask, "Screen_Time"] = df["Screen_Time"].median()

mask = (df["Social_Media_Time"] < 0) | (df["Social_Media_Time"] > 24)
df.loc[mask, "Social_Media_Time"] = df["Social_Media_Time"].median()

mask = (df["Focus_Score"] < 0) | (df["Focus_Score"] >= 10)
df.loc[mask, "Focus_Score"] = df["Focus_Score"].median()


#Shorting Data by Date
df=df.sort_values("Date")

df=df.reset_index(drop=True)

df.to_csv("Productivity_cleaned.csv", index=False)
print(df)