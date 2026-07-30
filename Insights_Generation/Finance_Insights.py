import pandas as pd
from datetime import datetime

df=pd.read_csv("../Feature_Engineering/Finance_Feature_Engineering.csv")
df["Date"]=datetime.now().date()

#calculate basic statistics
total_income=df["Income"].sum()
total_food=df["Food"].sum()
total_shopping=df["Shopping"].sum()
total_transport=df["Transport"].sum()
total_entertainment=df["Entertainment"].sum()
total_bill_Paid=df["Bill_Paid"].sum()
total_savings=df["Savings"].sum()

#calculate average
avg_income=df["Income"].mean()
avg_expense=(
    df["Food"]+
    df["Shopping"]+
    df["Transport"]+
    df["Entertainment"]
).mean()

avg_savings=df["Savings"].mean()

#calculate total expenses
df["Total_Expense"]=(
    df["Food"]+
    df["Shopping"]+
    df["Transport"]+
    df["Entertainment"]
)

total_expense=df["Total_Expense"].sum()

#highest expense day
highest_expense_day=df.loc[
    df["Total_Expense"].idxmax(),
    ["Date", "Total_Expense"]
]

#lowest expense day
lowest_expense_day=df.loc[
    df["Total_Expense"].idxmin(),
    ["Date", "Total_Expense"]
]

#highest saving day
highest_saving_day=df.loc[
    df["Savings"].idxmax(),
    ["Date", "Savings"]
]

#lowest saving day
lowest_saving_day=df.loc[
    df["Savings"].idxmin(),
    ["Date", "Savings"]
]

#biggest spending category
category_totals={
    "Food":total_food,
    "Shopping":total_shopping,
    "Transport":total_transport,
    "Entertainment":total_entertainment
}

biggest_category=max(category_totals, key=category_totals.get)

#calculate saving rate
savings_rate=round((total_savings/total_income)*100, 2)

#find days with savings
savings_days=(df["Savings"]>0).sum()

#find days overspending
overspending_days=(
    df["Total_Expense"]>df["Income"]
).sum()

finance_insights = {
    "Total Income": total_income,
    "Total Expense": total_expense,
    "Total Savings": total_savings,
    "Average Income": avg_income,
    "Average Expense": avg_expense,
    "Average Savings": avg_savings,
    "Highest Expense Day": highest_expense_day,
    "Lowest Expense Day": lowest_expense_day,
    "Highest Savings Day": highest_saving_day,
    "Lowest Savings Day": lowest_saving_day,
    "Biggest Spending Category": biggest_category,
    "Savings Rate (%)": savings_rate,
    "Saving Days": savings_days,
    "Overspending Days": overspending_days
}

insights_df = pd.DataFrame(
    finance_insights.items(),
    columns=["Insight", "Value"]
)

insights_df.to_csv("../Insights_Generation/Finance_insights.csv", index=False)

print("Insights saved successfully!")