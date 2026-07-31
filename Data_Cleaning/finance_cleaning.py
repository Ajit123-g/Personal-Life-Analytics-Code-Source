import pandas as pd

df=pd.read_csv("Data_Collection/Finance.csv")

cols=["Income", "Food", "Shopping", "Transport", "Entertainment", "Savings", "Bill_Paid"]

df=df.drop_duplicates()


#converting columns to numeric values
for col in cols:
    df[col]=pd.to_numeric(df[col], errors="coerce")

#handling missing values
for col in cols:
    df[col]=df[col].fillna(df[col].median())

#removing negetive values
for col in cols:
    df.loc[df[col]<0, col]=None
    df[col].fillna(df[col].median())

#cutting extra space
columns=df.columns.str.strip()


#reset index
df=df.reset_index(drop=True)

df.to_csv("Data_Cleaning/Finance_cleaned.csv", index=False)
print(df.describe())