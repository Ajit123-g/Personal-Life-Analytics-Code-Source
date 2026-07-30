import pandas as pd
from datetime import datetime

df=pd.read_csv("../Feature_Engineering/Habit_Feature_Engineering.csv")
df["Date"]=datetime.now().date()

#calculate Average Time Spent on each Habit
df["Coding_Minutes"]=df["Coding_Hours"]*60
habit_columns=[
    "Medition_Minutes",
    "Gym_Minutes",
    "Coding_Minutes",
    "Reading_Minutes",
    "Journaling_Minutes"
]
avg_habit=df[habit_columns].mean().round(2)
print(avg_habit)

#most practiced habit
most_practiced_habit=avg_habit.idxmax()
print(most_practiced_habit)

#least practiced habit
least_practiced_habit=avg_habit.idxmin()
print(least_practiced_habit)

#total time spend on each habit
total_habit_time=df[habit_columns].sum()
print(total_habit_time)

#calculte daily habit score
df["Habit_Score"]=(
    df["Medition_Minutes"]+
    df["Gym_Minutes"]+
    df["Coding_Minutes"]+
    df["Reading_Minutes"]+
    df["Journaling_Minutes"]
)
print(df[["Date", "Habit_Score"]])

#best habit Day
best_habit_day=df.loc[df["Habit_Score"].idxmax()]
print(best_habit_day)

#lowest habit day
worst_habit_day=df.loc[df["Habit_Score"].idxmin()]
print(worst_habit_day)

#active habit days
avg_score=df["Habit_Score"].mean()
active_days=df[
    df["Habit_Score"]>avg_score
]

print(len((active_days)))

#find maximum achievement
highest_coding=df["Coding_Hours"].max()
highest_gym=df["Gym_Minutes"].max()
highest_medition=df["Medition_Minutes"].max()


habit_insights = {
"Average Meditation": round(df["Medition_Minutes"].mean(),2),
"Average Gym": round(df["Gym_Minutes"].mean(),2),
"Average Coding Hours": round(df["Coding_Hours"].mean(),2),
"Average Reading": round(df["Reading_Minutes"].mean(),2),
"Average Journaling": round(df["Journaling_Minutes"].mean(),2),

"Most Practiced Habit": most_practiced_habit,
"Least Practiced Habit": least_practiced_habit,

"Best Habit Day": str(best_habit_day["Date"]),
"Worst Habit Day": str(worst_habit_day["Date"]),

"Highest Habit Score": int(df["Habit_Score"].max())

}

print(habit_insights)

insights_df = pd.DataFrame(
    habit_insights.items(),
    columns=["Insight", "Value"]
)

insights_df.to_csv("../Insights_Generation/Habit_insights.csv", index=False)

print("Insights saved successfully!")