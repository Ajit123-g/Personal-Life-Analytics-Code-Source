import pandas as pd

df=pd.read_csv("../Data_Collection/Habit_Tracker.csv")

cols=["Medition_Minutes", "Gym_Minutes", "Coding_Hours", "Reading_Minutes", "Journaling_Minutes"]

df=df.drop_duplicates()


#Convert hour columns to numbers
df["Wake-Up_Time"]=pd.to_datetime(df["Wake-Up_Time"], format="%H:%M", errors="coerce").dt.time
for col in cols:
    df[col]=pd.to_numeric(df[col], errors="coerce")

#Handling missing values
df["Wake-Up_Time"]=df["Wake-Up_Time"].fillna(pd.to_datetime("7:00", format="%H:%M").time())
for col in cols:
    df[col]=df[col].fillna(df[col].median())


#Detecting invalid values
mask = (df["Medition_Minutes"] < 0) | (df["Medition_Minutes"] > 300)
df.loc[mask, "Medition_Minutes"] = df["Medition_Minutes"].median()

mask = (df["Gym_Minutes"] < 0) | (df["Gym_Minutes"] > 300)
df.loc[mask, "Gym_Minutes"] = df["Gym_Minutes"].median()

mask = (df["Coding_Hours"] < 0) | (df["Coding_Hours"] > 24)
df.loc[mask, "Coding_Hours"] = df["Coding_Hours"].median()


mask = (df["Reading_Minutes"] < 0) | (df["Reading_Minutes"] > 300)
df.loc[mask, "Reading_Minutes"] = df["Reading_Minutes"].median()

mask = (df["Journaling_Minutes"] < 0) | (df["Journaling_Minutes"] > 300)
df.loc[mask, "Journaling_Minutes"] = df["Journaling_Minutes"].median()



df=df.reset_index(drop=True)


df.to_csv("Habit_cleaned.csv", index=False)
print(df)