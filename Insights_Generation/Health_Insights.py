import pandas as pd
from datetime import datetime


df=pd.read_csv("../Feature_Engineering/Health_Feature_Engineering.csv")
df["Date"]=datetime.now().date()

#Calculate Overall Statistics
Sleep_Hours_mean=df["Sleep_Hours"].mean()
Water_Intake_mean=df["Water_Intake"].mean()
Steps_mean=df["Steps"].mean()
Weight_mean=df["Weight"].mean()
Calories_mean=df["Calories"].mean()

#for maximum
Sleep_Hours_maximum=df["Sleep_Hours"].max()
Water_Intake_maximum=df["Water_Intake"].max()
Steps_maximum=df["Steps"].max()
Weight_maximum=df["Weight"].max()
Calories_maximum=df["Calories"].max()


#for  minimum
Sleep_Hours_minimum=df["Sleep_Hours"].min()
Water_Intake_minimum=df["Water_Intake"].min()
Steps_minimum=df["Steps"].min()
Weight_minimum=df["Weight"].min()
Calories_minimum=df["Calories"].min()

#Healthiest Day
Healthiest_Day=df[
    (df["Mood"]=="Happy")&
    (df["Stress_Level"]=="Low")&
    (df["Sleep_Hours"]>=7)
]
print(Healthiest_Day[["Date", "Mood", "Stress_Level", "Sleep_Hours"]])

# print("Healthest Days : ", df["Stress_Level"].mode())

#Unhealthy Day
#Day with highest calories
highest_calories_day=df.loc[df["Calories"].idxmax(), ["Date", "Calories"]]
print(highest_calories_day)

#Day with lowest steps
lowest_steps_day=df.loc[df["Steps"].idxmax(), ["Date", "Steps"]]
print(lowest_steps_day)

#Day with lowest water intake
lowest_water_intake_day=df.loc[df["Water_Intake"].idxmax(), ["Date", "Water_Intake"]]
print(lowest_water_intake_day)

#Day with highest stress
stress_order={
    "Low":1,
    "Medium":2,
    "High":3
}
df["Stress_Score"]=df["Stress_Level"].map(stress_order)
high_stress_day=df.loc[df["Stress_Score"].idxmax(), ["Date", "Stress_Level"]]
print(high_stress_day)

#weekly analysis
df["Date"]=pd.to_datetime(df["Date"], format="%d-%m-%Y")
df["Week"]=df["Date"].dt.isocalendar().week
weekly_analysis=df.groupby("Week")[[
    "Sleep_Hours",
    "Water_Intake",
    "Steps",
    "Weight",
    "Calories"
]].mean()

print(weekly_analysis)

#average health
print("Average Sleep:", round(df["Sleep_Hours"].mean(), 2), "hours")
print("Average Water Intake:", round(df["Water_Intake"].mean(), 2), "L")
print("Average Steps:", round(df["Steps"].mean(), 0))
print("Average Calories:", round(df["Calories"].mean(), 0))
print("Average Weight:", round(df["Weight"].mean(), 2), "kg")

###Best Health Day
df["Health_Score"]=(
    df["Sleep_Hours"]*0.30+
    df["Water_Intake"]*0.20+
    (df["Steps"]/1000)*0.30+
    (df["Calories"]/1000)*0.20
)

#Best Day
best_day=df.loc[df["Health_Score"].idxmax()]
print("Best Health Day : ", best_day["Date"].strftime("%d-%m-%Y"))

#Worst Day
Worst_Day=df.loc[df["Health_Score"].idxmin()]
print("Worst Health Day : ", Worst_Day["Date"].strftime("%d-%m-%Y"))

#Highest Step Count
Highest_Step_day=df.loc[df["Steps"].idxmax()]
print("Highest Steps Count : ", Highest_Step_day["Date"].strftime("%d-%m-%Y"))

#Lowest Water Intake
Lowest_Water_Intake=df.loc[df["Water_Intake"].idxmin()]
print("Lowest Water Intake : ", Lowest_Water_Intake["Date"].strftime("%d-%m-%Y"))

#Most Common Mood
print("Most Common Mood : ", df["Mood"].mode()[0])

#Most Common Stress Level
print("Most Common Stress Level : ", df["Stress_Level"].mode()[0])

#Active Days
active_days=df[df["Steps"]>=10000]
print("Active Days : ", len(active_days))

#best week
Best_Week=df.loc[df["Health_Score"].idxmax()]
print("Best Week : ", Best_Week["Week"])

#################################################
health_insights = {
    # Average Health Metrics
    "Average Sleep Hours": round(df["Sleep_Hours"].mean(), 2),
    "Average Water Intake": round(df["Water_Intake"].mean(), 2),
    "Average Steps": round(df["Steps"].mean(), 0),
    "Average Calories": round(df["Calories"].mean(), 0),
    "Average Weight": round(df["Weight"].mean(), 2),

    # Best and Worst Health Performance
    "Best Health Day": best_day["Date"].strftime("%d-%m-%Y"),
    "Worst Health Day": Worst_Day["Date"].strftime("%d-%m-%Y"),

    # Activity Insights
    "Highest Step Count": int(df["Steps"].max()),
    "Highest Step Day": Highest_Step_day["Date"].strftime("%d-%m-%Y"),
    "Active Days (>=10000 steps)": len(active_days),

    # Hydration Insights
    "Lowest Water Intake": float(df["Water_Intake"].min()),
    "Lowest Water Intake Day": Lowest_Water_Intake["Date"].strftime("%d-%m-%Y"),

    # Lifestyle Insights
    "Most Common Mood": df["Mood"].mode()[0],
    "Most Common Stress Level": df["Stress_Level"].mode()[0],

    # Stress Analysis
    "Highest Stress Day": high_stress_day["Date"].strftime("%d-%m-%Y"),
    "Highest Stress Level": high_stress_day["Stress_Level"]

    # # Weekly Performance
    # "Best Week": Best_Week["Health_Score"].idxmax() 
}

health_insights_df = pd.DataFrame(
    list(health_insights.items()),
    columns=["Insight", "Value"]
)

health_insights_df.to_csv("../Insights_Generation/Health_insights.csv")

print(health_insights_df)