import pandas as pd
from datetime import datetime
import os

today=datetime.now().strftime("%d-%m-%y")
study_hours=float(input("Study_Hours : "))
coding_hours=float(input("Coding_Hours : "))
exercise_minutes=float(input("Exercise_Minutes : "))
reading_minutes=float(input("Reading_Minutes : "))
screen_time=float(input("Screen_Time : "))
social_media_time=float(input("Social_Media_Time : "))
focus_score=float(input("Focus_Score : "))


Data={
    'Date':[today],
    'Study_Hours':[study_hours],
    'Coding_Hours':[coding_hours],
    'Exercise_Minutes':[exercise_minutes],
    'Reading_Minutes':[reading_minutes],
    'Screen_Time':[screen_time],
    'Social_Media_Time':[social_media_time],
    'Focus_Score':[focus_score]
}

df=pd.DataFrame(Data)
file_name="Productivity.csv"
if os.path.exists(file_name):
    #Add new row without writting the header again
    df.to_csv(file_name, mode='a', header=False, index=False)
else:
    #Create the file with header
    df.to_csv(file_name, mode="w", header=True, index=False)
print(df)