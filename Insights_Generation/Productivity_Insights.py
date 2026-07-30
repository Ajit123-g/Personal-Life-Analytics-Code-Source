import pandas as pd

df=pd.read_csv("../Feature_Engineering/Productivity_Feature_Engineering.csv")

#Calculate Overall Statistics
Study_Hours_mean=df["Study_Hours"].mean()
Coding_Hours_mean=df["Coding_Hours"].mean()
Exercise_Minutes_mean=df["Exercise_Minutes"].mean()
Reading_Minutes_mean=df["Reading_Minutes"].mean()
Screen_Time_mean=df["Screen_Time"].mean()
Social_Media_Time_mean=df["Social_Media_Time"].mean()
Focus_Score_mean=df["Focus_Score"].mean()

#for maximum
Study_Hours_maximum=df["Study_Hours"].max()
Coding_Hours_maximum=df["Coding_Hours"].max()
Exercise_Minutes_maximum=df["Exercise_Minutes"].max()
Reading_Minutes_maximum=df["Reading_Minutes"].max()
Screen_Time_maximum=df["Screen_Time"].max()
Social_Media_Time_maximum=df["Social_Media_Time"].max()
Focus_Score_maximum=df["Focus_Score"].max()

#for  minimum
Study_Hours_minimum=df["Study_Hours"].min()
Coding_Hours_minimum=df["Coding_Hours"].min()
Exercise_Minutes_minimum=df["Exercise_Minutes"].min()
Reading_Minutes_minimum=df["Reading_Minutes"].min()
Screen_Time_minimum=df["Screen_Time"].min()
Social_Media_Time_minimum=df["Social_Media_Time"].min()
Focus_Score_minimum=df["Focus_Score"].min()

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

# print(df["Productivity_Category"].value_counts())


#Weekly Performance
#Study_Hours
df["Date"]=pd.to_datetime(df["Date"])
weekly=df.groupby(df["Date"].dt.isocalendar().week)[["Study_Hours", "Coding_Hours", "Focus_Score", "Reading_Minutes", "Screen_Time"]].mean().round(2)
print(weekly)

#Best ans Worst Days
best_day=df.loc[df["Focus_Score"].idxmax()]

worst_day=df.loc[df["Focus_Score"].idxmin()]

#Trend Analysis
#study_hours
df["Study_Rolling"]=df["Study_Hours"].rolling(7).mean()

#Coding_Hours
df["Coding_Rolling"]=df["Coding_Hours"].rolling(7).mean()

#Reading_Minutes
df["Reading_Rolling"]=df["Reading_Minutes"].rolling(7).mean()

#Screen_Time
df["Screen_Rolling"]=df["Screen_Time"].rolling(7).mean()

#Focus_Score
df["Focus_Rolling"]=df["Focus_Score"].rolling(7).mean()

#Insights 
#Key Matrics
print(f"Average Study Hours : {df["Study_Hours"].mean() : .2f} hrs")
print(f"Average Coding Hours : {df["Coding_Hours"].mean() : .2f} hrs")
print(f"Average Focus Score : {df["Focus_Score"].mean() : .2f}")
print(f"Average Screen Time : {df["Screen_Time"].mean() : .2f} hrs")

#Best Performance
highest_focus=df["Focus_Score"].max()
print(f"Highest Focus Score : ", highest_focus)

best_day=df.loc[df["Focus_Score"].idxmax()]
print(f"Most Productive Day : ", best_day["Date"].strftime("%d-%m-%Y"))

highest_Study=df["Study_Hours"].max()
print(f"Highest Study Hours : ", highest_Study)

highest_Coding=df["Coding_Hours"].max()
print(f"Highest Coding Hours : ", highest_Coding)

insights = {
    "Average Study Hours": Study_Hours_mean,
    "Average Coding Hours": Coding_Hours_mean,
    "Average Focus Score": Focus_Score_mean,
    "Average Screen Time": Screen_Time_mean,

    "Highest Study Hours": Study_Hours_maximum,
    "Highest Coding Hours": Coding_Hours_maximum,
    "Highest Focus Score": Focus_Score_maximum,

    "Lowest Study Hours": Study_Hours_minimum,
    "Lowest Coding Hours": Coding_Hours_minimum,
    "Lowest Focus Score": Focus_Score_minimum,

    "Most Productive Day": best_day["Date"].strftime("%d-%m-%Y")
}

insights_df = pd.DataFrame(
    insights.items(),
    columns=["Metric", "Value"]
)

insights_df.to_csv("../Insights_Generation/Productivity_insights.csv")