import pandas as pd
import os

medition_minutes=float(input("Medition_Minutes : "))
gym_minutes=float(input("Gym_Minutes : "))
coding_hours=float(input("Coding_Hours : "))
reading_minutes=float(input("Reading_Minutes : "))
journaling_minutes=float(input("Journaling_Minutes : "))
wakeup_time=input("Wake-Up_Time(HH:MM) : ")


data={
    'Medition_Minutes':[medition_minutes],
    'Gym_Minutes':[gym_minutes],
    'Coding_Hours':[coding_hours],
    'Reading_Minutes':[reading_minutes],
    'Journaling_Minutes':[journaling_minutes],
    'Wake-Up_Time':[wakeup_time]
}

df=pd.DataFrame(data)
file_name="Habit_Tracker.csv"
#Method to Update columns
#df.rename(columns={"Coding_Minutes":"Coding_Hours"}, inplace=True)
#df.to_csv(file_name, index=False)

if os.path.exists(file_name):
    df.to_csv(file_name, mode="a", header=False, index=False)

else:
    df.to_csv(file_name, mode="w", header=True, index=False)


print(df)