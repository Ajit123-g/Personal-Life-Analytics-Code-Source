import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Data_Cleaning/Productivity_cleaned.csv")

sns.set_style("whitegrid")

#########graph for univariate

# #study hours
plt.figure(figsize=(8,5))
sns.histplot(df["Study_Hours"], bins=10, kde=True)
plt.title("Study Hours Distribution")
plt.xlabel("Study_Hours")
plt.ylabel("Count")
plt.savefig("graphs/Productivity/Study_Hours_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Coding_Hours
plt.figure(figsize=(8,5))
sns.histplot(df["Coding_Hours"], bins=10, kde=True)
plt.title("Coding Hours Distribution")
plt.xlabel("Coding_Hours")
plt.ylabel("Count")
plt.savefig("graphs/Productivity/Coding_Hours_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Exercise_Minutes
plt.figure(figsize=(8,5))
sns.histplot(df["Exercise_Minutes"], bins=10, kde=True)
plt.title("Exercise Minutes Distribution")
plt.xlabel("Exercise_Minutes")
plt.ylabel("Count")
plt.savefig("graphs/Productivity/Exercise_Minutes_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Reading_Minutes
plt.figure(figsize=(8,5))
sns.histplot(df["Reading_Minutes"], bins=10, kde=True)
plt.title("Reading Minutes Distribution")
plt.xlabel("Reading_Minutes")
plt.ylabel("Count")
plt.savefig("graphs/Productivity/Reading_Minutes_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Screen_Time
plt.figure(figsize=(8,5))
sns.histplot(df["Screen_Time"], bins=10, kde=True)
plt.title("Screen Time Distribution")
plt.xlabel("Screen_Time")
plt.ylabel("Count")
plt.savefig("graphs/Productivity/Screen_Time_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Social_Media_Time
plt.figure(figsize=(8,5))
sns.histplot(df["Social_Media_Time"], bins=10, kde=True)
plt.title("Social Media Time Distribution")
plt.xlabel("Social_Media_Time")
plt.ylabel("Count")
plt.savefig("graphs/Productivity/Social_Media_Time_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Focus_Score
plt.figure(figsize=(8,5))
sns.histplot(df["Focus_Score"], bins=10, kde=True)
plt.title("Focus Score Distribution")
plt.xlabel("Focus_Score")
plt.ylabel("Count")
plt.savefig("graphs/Productivity/Focus_Score_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


########graph for outliers

# #Study_Hours
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Study_Hours"])
plt.title("Study Hours Outliers")
plt.savefig("graphs/Productivity/Study_Hours_Box.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Coding_Hours
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Coding_Hours"])
plt.title("Coding Hours Outliers")
plt.savefig("graphs/Productivity/Coding_Hours_Box.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Exercise_Minutes
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Exercise_Minutes"])
plt.title("Exercise Minutes Outliers")
plt.savefig("graphs/Productivity/Exercise_Minutes_Box.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Reading_Minutes
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Reading_Minutes"])
plt.title("Reading Minutes Outliers")
plt.savefig("graphs/Productivity/Reading_Minutes_Box.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Screen_Time
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Screen_Time"])
plt.title("Screen Time Outliers")
plt.savefig("graphs/Productivity/Screen_Time_Box.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Focus_Score
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Focus_Score"])
plt.title("Focus Score Outliers")
plt.savefig("graphs/Productivity/Focus_Score_Box.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

######correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("graphs/Productivity/Correlation_Heatmap.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#####study_hours vs focus_score
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Study_Hours",
    y="Focus_Score",
    data=df
)
plt.title("Study_Hours vs Focus_Score")
plt.savefig("graphs/Productivity/study_hours_vs_focus_score.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


# #coding_hours vs focus_score
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Coding_Hours",
    y="Focus_Score",
    data=df
)
plt.title("Coding_Hours vs Focus_Score")
plt.savefig("graphs/Productivity/coding_hours_vs_focus_score.png",
            dpi=300,
            bbox_inches="tight")
plt.show()



# #reading vs focus_score
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Reading_Minutes",
    y="Focus_Score",
    data=df
)
plt.title("Reading_Minutes vs Focus_Score")
plt.savefig("graphs/Productivity/reading_vs_focus_score.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


# #screen_time vs focus_score
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Screen_Time",
    y="Focus_Score",
    data=df
)
plt.title("Screen_Time vs Focus_Score")
plt.savefig("graphs/Productivity/screen_time_vs_focus_score.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


# #social_media_time vs focus_score
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Social_Media_Time",
    y="Focus_Score",
    data=df
)
plt.title("Social_Media_Time vs Focus_Score")
plt.savefig("graphs/Productivity/social_media_time_vs_focus_score.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


# #exercise vs focus_score
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Exercise_Minutes",
    y="Focus_Score",
    data=df
)
plt.title("Exercise_Minutes vs Focus_Score")
plt.savefig("graphs/Productivity/exercise_vs_focus_score.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

###line chart(trend over time)
##Study_Hours
plt.figure(figsize=(7, 5))
plt.plot(df["Date"], df["Study_Hours"])
plt.title("Study Hours over Time")
plt.xticks(rotation=45)
plt.savefig("graphs/Productivity/Study_Hours_line_chart.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

##Coding_Hours
plt.figure(figsize=(7, 5))
plt.plot(df["Date"], df["Coding_Hours"])
plt.title("Coding Hours over Time")
plt.xticks(rotation=45)
plt.savefig("graphs/Productivity/Coding_Hours_line_chart.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

##Reading_Minutes
plt.figure(figsize=(7, 5))
plt.plot(df["Date"], df["Reading_Minutes"])
plt.title("Reading Minutes over Time")
plt.xticks(rotation=45)
plt.savefig("graphs/Productivity/Reading_Minutes_line_chart.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

##Screen_Time
plt.figure(figsize=(7, 5))
plt.plot(df["Date"], df["Screen_Time"])
plt.title("Screen Time over Time")
plt.xticks(rotation=45)
plt.savefig("graphs/Productivity/Screen_Time_line_chart.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

##Social_Media_Time
plt.figure(figsize=(7, 5))
plt.plot(df["Date"], df["Social_Media_Time"])
plt.title("Social Media over Time")
plt.xticks(rotation=45)
plt.savefig("graphs/Productivity/Social_Media_Time_line_chart.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

##Exercise_Minutes
plt.figure(figsize=(7, 5))
plt.plot(df["Date"], df["Exercise_Minutes"])
plt.title("Exercise Minutes over Time")
plt.xticks(rotation=45)
plt.savefig("graphs/Productivity/Exercise_Minutes_line_chart.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

##focus_score
plt.figure(figsize=(7, 5))
plt.plot(df["Date"], df["Focus_Score"])
plt.title("focus score over Time")
plt.xticks(rotation=45)
plt.savefig("graphs/Productivity/focus_score_line_chart.png",
            dpi=300,
            bbox_inches="tight")
plt.show()