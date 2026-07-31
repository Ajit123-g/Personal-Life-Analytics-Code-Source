import pandas as pd

df=pd.read_csv("Data_Cleaning/Finance_cleaned.csv")

#create Total Expenses
df["Total_Expenses"]=(
    df["Food"]+
    df["Transport"]+
    df["Shopping"]+
    df["Entertainment"]
)

#Create Net Saving
df["Net_Savings"]=(
    df["Savings"]
)

#Create Saving Rate
df["Savings_Rate"]=((
    df["Net_Savings"]/df["Income"]
)*100).round(2)

#Create Expense Rate
df["Expense_Rate"]=((
    df["Total_Expenses"]/df["Income"]
)*100).round(2)

#Create Highest Expense Category
Expense_cols=["Food", "Transport", "Shopping", "Entertainment"]
df["Highest_Expense"]=df[Expense_cols].idxmax(axis=1)

#Create Finance Health Flag
df["Good_Financial_Day"]=(
    df["Net_Savings"]>0
).astype(int)


df.to_csv(
    "Feature_Engineering/Finance_Feature_Engineering.csv",
    index=False
)