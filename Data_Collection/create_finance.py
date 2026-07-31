import pandas as pd
import os

income=float(input("Income : "))
food=float(input("Food : "))
shopping=float(input("Shopping : "))
transport=float(input("Transport : "))
entertainment=float(input("Entertainment : "))
bill_paid=float(input("Bill_Paid : "))

Data={
    'Income':[income],
    'Food':[food],
    'Shopping':[shopping],
    'Transport':[transport],
    'Entertainment':[entertainment],
    'Bill_Paid':[bill_paid],
    'Savings':[income-food-shopping-transport-entertainment-bill_paid]
}

df=pd.DataFrame(Data)


file_name="Finance.csv"
if os.path.exists(file_name):
    #executed when file exist
    df.to_csv(file_name, mode="a", header=False, index=False)

else:
    #executed when file not exist
    df.to_csv(file_name, mode="w", header=True, index=False)

print(df)