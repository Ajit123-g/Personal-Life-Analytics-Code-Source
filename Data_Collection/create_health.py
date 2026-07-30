import pandas as pd
import os

sleep_hours=float(input("Sleep_Hours : "))
water_intake=float(input("Water_Intake : "))
steps=float(input("Steps : "))
weight=float(input("Weight : "))
calories=float(input("Calories : "))
mood=input("Mood : ")
stress_level=input("Stress_Level : ")

data={
    'Sleep_Hours':[sleep_hours],
    'Water_Intake':[water_intake],
    'Steps':[steps],
    'Weight':[weight],
    'Calories':[calories],
    'Mood':[mood],
    'Stress_Level':[stress_level]
}

df=pd.DataFrame(data)
file_name="Health.csv"

if os.path.exists(file_name):
    #executed when Health.csv file exist
    df.to_csv(file_name, mode="a", header=False, index=False)

else:
    #executed when Health.csv file does not exist
    df.to_csv(file_name, mode="w", header=True, index=False)

print(df)