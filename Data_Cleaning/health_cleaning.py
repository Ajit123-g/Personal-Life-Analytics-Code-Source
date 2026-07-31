import pandas as pd

df=pd.read_csv("Data_Collection/Health.csv")

cols=["Sleep_Hours", "Water_Intake", "Steps", "Weight", "Calories"]

df=df.drop_duplicates()

#Replacing Mood input to standard level
df["Mood"]=df["Mood"].replace({
    "sad":"Sad",
    "s":"Sad",
    "S":"Sad",
    "SAD":"Sad",
    "Sad":"Sad",

    "happy":"Happy",
    "h":"Happy",
    "H":"Happy",
    "HAPPY":"Happy",
    "Happy":"Happy",

    "neutral":"Neutral",
    "n":"Neutral",
    "N":"Neutral",
    "Neutral":"Neutral",
    "NEUTRAL":"Neutral"
})


#Replacing Stress_Level input to standard level
df["Stress_Level"]=df["Stress_Level"].replace({
    "low":"Low",
    "l":"Low",
    "L":"Low",
    "LOW":"Low",
    "Low":"Low",

    "medium":"Medium",
    "m":"Medium",
    "M":"Medium",
    "MEDIUM":"Medium",
    "Medium":"Medium",

    "high":"High",
    "h":"High",
    "H":"High",
    "High":"High",
    "HIGH":"High"
})

#handling invalid values
mask=(df["Sleep_Hours"]<1) | (df["Sleep_Hours"]>15)
df.loc[mask, "Sleep_Hours"]=df["Sleep_Hours"].median()

mask=(df["Water_Intake"]<0) | (df["Water_Intake"]>10)
df.loc[mask, "Water_Intake"]=df["Water_Intake"].median()

mask=(df["Steps"]<0) | (df["Steps"]>100000)
df.loc[mask, "Steps"]=df["Steps"].median()

mask=(df["Weight"]<0) | (df["Weight"]>150)
df.loc[mask, "Weight"]=df["Weight"].median()

mask=(df["Calories"]<20) | (df["Calories"]>10000)
df.loc[mask, "Calories"]=df["Calories"].median()

valid_moods=["s", "S", "sad", "SAD", "Sad", "h", "H", "happy", "Happy", "HAPPY", "n", "N", "neutral", "Neutral", "NEUTRAL"]
#replacing invalid value with NaN
df.loc[~df["Mood"]. isin(valid_moods), "Mood"]=pd.NA
#filling missing value of mood
df["Mood"]=df["Mood"].fillna(df["Mood"].mode([])[0])

valid_stress=["l", "L", "low", "LOW", "Low", "m", "M", "medium", "Medium", "MEDIUM", "h", "H", "high", "High", "HIGH"]
#replacing invalid value with NaN
df.loc[~df["Stress_Level"]. isin(valid_stress), "Stress_Level"]=pd.NA
#filling missing value of Stress_Level
df["Stress_Level"]=df["Stress_Level"].fillna(df["Stress_Level"].mode([])[0])



#converting the columns to numeric
for col in cols:
    df[col]=pd.to_numeric(df[col], errors="coerce")

#missing value handling
for col in cols:
    df[col]=df[col].fillna(df[col].median())

#reset index
df.reset_index(drop=True, inplace=True)


df.to_csv("Data_Cleaning/Health_cleaned.csv", index=False)

print(df)