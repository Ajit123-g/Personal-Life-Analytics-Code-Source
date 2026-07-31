import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Data_Cleaning/Health_cleaned.csv")

sns.set_style("whitegrid")

#########graph for univariate
#Sleep_Hours,Water_Intake,Steps,Weight,Calories
# #Sleep_Hours
plt.figure(figsize=(8,5))
sns.histplot(df["Sleep_Hours"], bins=10, kde=True)
plt.title("Sleep Hours Distribution")
plt.xlabel("Sleep_Hours")
plt.ylabel("Count")
plt.savefig("graphs/Health/Sleep_Hours_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Water_Intake
plt.figure(figsize=(8,5))
sns.histplot(df["Water_Intake"], bins=10, kde=True)
plt.title("Water Intake Distribution")
plt.xlabel("Water_Intake")
plt.ylabel("Count")
plt.savefig("graphs/Health/Water_Intake_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Steps
plt.figure(figsize=(8,5))
sns.histplot(df["Steps"], bins=10, kde=True)
plt.title("Steps Distribution")
plt.xlabel("Steps")
plt.ylabel("Count")
plt.savefig("graphs/Health/Steps_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Weight
plt.figure(figsize=(8,5))
sns.histplot(df["Weight"], bins=10, kde=True)
plt.title("Weight Distribution")
plt.xlabel("Weight")
plt.ylabel("Count")
plt.savefig("graphs/Health/Weight_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Calories
plt.figure(figsize=(8,5))
sns.histplot(df["Calories"], bins=10, kde=True)
plt.title("Calories Distribution")
plt.xlabel("Calories")
plt.ylabel("Count")
plt.savefig("graphs/Health/Calories_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#########Box Plot
#Sleep_Hours,Water_Intake,Steps,Weight,Calories
# #Sleep_Hours
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Sleep_Hours"])
plt.title("Sleep Hours Box Plot")
plt.savefig("graphs/Health/Sleep_Hours_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Water_Intake
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Water_Intake"])
plt.title("Water Intake Box Plot")
plt.savefig("graphs/Health/Water_Intake_boxplot.png",
            dpi=300,
            bbox_inches="tight")

# #Steps
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Steps"])
plt.title("Steps Box Plot")
plt.savefig("graphs/Health/Steps_boxplot.png",
            dpi=300,
            bbox_inches="tight")

# #Weight
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Weight"])
plt.title("Weight Box Plot")
plt.savefig("graphs/Health/Weight_boxplot.png",
            dpi=300,
            bbox_inches="tight")

# #Calories
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Calories"])
plt.title("Calories Box Plot")
plt.savefig("graphs/Health/Calories_boxplot.png",
            dpi=300,
            bbox_inches="tight")

######Categorical Graphs

# #Mood
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Mood")
plt.title("Mood Count")
plt.savefig("graphs/Health/Mood_countplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Stress_Level
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Stress_Level")
plt.title("Stress_Level Count")
plt.savefig("graphs/Health/Stress_Level_countplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


#####Bivariate analysis
#sleep vs mood
plt.figure(figsize=(8, 5))
sns.boxplot(x="Mood", y="Sleep_Hours", data=df)
plt.title("Mood vs Sleep_Hours")
plt.savefig("graphs/Health/Mood_vs_Sleep_Hours_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#sleep vs stress
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Stress_Level", y="Sleep_Hours", data=df)
plt.title("Stress_Level vs Sleep_Hours")
plt.savefig("graphs/Health/Stress_Level_vs_Sleep_Hours_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#Calories vs Weight
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Calories", y="Weight", data=df)
plt.title("Calories vs Weight")
plt.savefig("graphs/Health/Calories_vs_Weight_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


######correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("graphs/Health/Correlation_Heatmap.png",
            dpi=300,
            bbox_inches="tight")
plt.show()