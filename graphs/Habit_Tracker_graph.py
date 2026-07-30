import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("../Data_Cleaning/Habit_cleaned.csv")

sns.set_style("whitegrid")


#########graph for univariate
#Medition_Minutes,Gym_Minutes,Coding_Hours,Reading_Minutes,Journaling_Minutes,Wake-Up_Time
# #Medition_Minutes
plt.figure(figsize=(8,5))
sns.histplot(df["Medition_Minutes"], bins=10, kde=True)
plt.title("Medition Minutes Distribution")
plt.xlabel("Medition_Minutes")
plt.ylabel("Count")
plt.savefig("../graphs/Habit_Tracker/Medition_Minutes_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Gym_Minutes
plt.figure(figsize=(8,5))
sns.histplot(df["Gym_Minutes"], bins=10, kde=True)
plt.title("Gym Minutes Distribution")
plt.xlabel("Gym_Minutes")
plt.ylabel("Count")
plt.savefig("../graphs/Habit_Tracker/Gym_Minutes_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Coding_Hours
plt.figure(figsize=(8,5))
sns.histplot(df["Coding_Hours"], bins=10, kde=True)
plt.title("Coding Hours Distribution")
plt.xlabel("Coding_Hours")
plt.ylabel("Count")
plt.savefig("../graphs/Habit_Tracker/Coding_Hours_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Reading_Minutes
plt.figure(figsize=(8,5))
sns.histplot(df["Reading_Minutes"], bins=10, kde=True)
plt.title("Reading Minutes Distribution")
plt.xlabel("Reading_Minutes")
plt.ylabel("Count")
plt.savefig("../graphs/Habit_Tracker/Reading_Minutes_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Journaling_Minutes
plt.figure(figsize=(8,5))
sns.histplot(df["Journaling_Minutes"], bins=10, kde=True)
plt.title("Journaling Minutes Distribution")
plt.xlabel("Journaling_Minutes")
plt.ylabel("Count")
plt.savefig("../graphs/Habit_Tracker/Journaling_Minutes_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#########Box Plot
#Medition_Minutes,Gym_Minutes,Coding_Hours,Reading_Minutes,Journaling_Minutes
# #Medition_Minutes
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Medition_Minutes"])
plt.title("Medition Minutes Box Plot")
plt.savefig("../graphs/Habit_Tracker/Medition_Minutes_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Gym_Minutes
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Gym_Minutes"])
plt.title("Water Intake Box Plot")
plt.savefig("../graphs/Habit_Tracker/Gym_Minutes_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Coding_Hours
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Coding_Hours"])
plt.title("Coding_Hours Box Plot")
plt.savefig("../graphs/Habit_Tracker/Coding_Hours_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Reading_Minutes
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Reading_Minutes"])
plt.title("Reading_Minutes Box Plot")
plt.savefig("../graphs/Habit_Tracker/Reading_Minutes_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Journaling_Minutes
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Journaling_Minutes"])
plt.title("Journaling_Minutes Box Plot")
plt.savefig("../graphs/Habit_Tracker/Journaling_Minutes_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

######correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("../graphs/Habit_Tracker/Correlation_Heatmap.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

######Categorical Graphs

# #Wake-Up_Time
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Wake-Up_Time")
plt.title("Wake-Up_Time Count")
plt.savefig("../graphs/Habit_Tracker/Wake-Up_Time_countplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()