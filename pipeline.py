import subprocess

# Data Cleaning
subprocess.run(["python", "Data_Cleaning/finance_cleaning.py"], check=True)
subprocess.run(["python", "Data_Cleaning/health_cleaning.py"], check=True)
subprocess.run(["python", "Data_Cleaning/habit_cleaning.py"], check=True)
subprocess.run(["python", "Data_Cleaning/productivity_cleaning.py"], check=True)

# Add EDA scripts
subprocess.run(["python", "EDA/Finance_eda.py"], check=True)
subprocess.run(["python", "EDA/Habit_Tracker_eda.py"], check=True)
subprocess.run(["python", "EDA/Health_eda.py"], check=True)
subprocess.run(["python", "EDA/Productivity_eda.py"], check=True)

# Add FEATURE ENGINEERING scripts
subprocess.run(["python", "Feature_Engineering/Finance_Feature.py"], check=True)
subprocess.run(["python", "Feature_Engineering/Habit_Tracker_Feature.py"], check=True)
subprocess.run(["python", "Feature_Engineering/Health_Feature.py"], check=True)
subprocess.run(["python", "Feature_Engineering/Productivity_Feature.py"], check=True)

# Add graph scripts
subprocess.run(["python", "graphs/Finance_graph.py"], check=True)
subprocess.run(["python", "graphs/Habit_Tracker_graph.py"], check=True)
subprocess.run(["python", "graphs/Health_graph.py"], check=True)
subprocess.run(["python", "graphs/Productivity_graph.py"], check=True)

# Add insights scripts
subprocess.run(["python", "Insights_Generation/Finance_insights.py"], check=True)
subprocess.run(["python", "Insights_Generation/Habit_Tracker_insights.py"], check=True)
subprocess.run(["python", "Insights_Generation/Health_insights.py"], check=True)
subprocess.run(["python", "Insights_Generation/Productivity_insights.py"], check=True)

print("Pipeline completed successfully!")