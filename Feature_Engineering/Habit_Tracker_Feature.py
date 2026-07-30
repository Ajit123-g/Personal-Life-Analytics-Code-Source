import pandas as pd

df=pd.read_csv("../Data_Cleaning/Habit_cleaned.csv")

#Total Habit Time 
df["Total_Habit_Time"]=(
    df["Medition_Minutes"]+
    df["Gym_Minutes"]+
    (df["Coding_Hours"]*60)+
    df["Reading_Minutes"]+
    df["Journaling_Minutes"]
)

#Wake-Up Hour
df["Wake-Up_Time"]=pd.to_datetime(
    df["Wake-Up_Time"]
)

df["Wake-Up_Hour"]=df["Wake-Up_Time"].dt.hour


#Early Riser
df["Early_Riser"]=(
    df["Wake-Up_Hour"]<=6
).astype(int)

#Habit Performance
df["Habit_Performance"]=pd.cut(
    df["Total_Habit_Time"],
    bins=[0, 120, 240, 1000],
    labels=["Low", "Medium", "High"]
)


df.to_csv(
    "../Feature_Engineering/Habit_Feature_Engineering.csv",
    index=False
)

print(df)