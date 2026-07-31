import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Data_Cleaning/Finance_cleaned.csv")

sns.set_style("whitegrid")

#########graph for univariate
#Income,Food,Shopping,Transport,Entertainment,Bill_Paid,Savings
# #Income
plt.figure(figsize=(8,5))
sns.histplot(df["Income"], bins=10, kde=True)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Count")
plt.savefig("graphs/Finance/Income_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Shopping
plt.figure(figsize=(8,5))
sns.histplot(df["Shopping"], bins=10, kde=True)
plt.title("Shopping Distribution")
plt.xlabel("Shopping")
plt.ylabel("Count")
plt.savefig("graphs/Finance/Shopping_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Transport
plt.figure(figsize=(8,5))
sns.histplot(df["Transport"], bins=10, kde=True)
plt.title("Transport Distribution")
plt.xlabel("Transport")
plt.ylabel("Count")
plt.savefig("graphs/Finance/Transport_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Entertainment
plt.figure(figsize=(8,5))
sns.histplot(df["Entertainment"], bins=10, kde=True)
plt.title("Entertainment Distribution")
plt.xlabel("Entertainment")
plt.ylabel("Count")
plt.savefig("graphs/Finance/Entertainment_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Bill_Paid
plt.figure(figsize=(8,5))
sns.histplot(df["Bill_Paid"], bins=10, kde=True)
plt.title("Bill Paid Distribution")
plt.xlabel("Bill_Paid")
plt.ylabel("Count")
plt.savefig("graphs/Finance/Bill_Paid_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Savings
plt.figure(figsize=(8,5))
sns.histplot(df["Savings"], bins=10, kde=True)
plt.title("Savings Distribution")
plt.xlabel("Savings")
plt.ylabel("Count")
plt.savefig("graphs/Finance/Savings_Histogram.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#########Box Plot
#Income,Shopping,Transport,Entertainment,Bill_Paid
# #Income
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Income"])
plt.title("Income Box Plot")
plt.savefig("graphs/Finance/Income_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Shopping
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Shopping"])
plt.title("Water Intake Box Plot")
plt.savefig("graphs/Finance/Shopping_boxplot.png",
            dpi=300,
            bbox_inches="tight")

# #Transport
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Transport"])
plt.title("Transport Box Plot")
plt.savefig("graphs/Finance/Transport_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Entertainment
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Entertainment"])
plt.title("Entertainment Box Plot")
plt.savefig("graphs/Finance/Entertainment_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Bill_Paid
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Bill_Paid"])
plt.title("Bill Paid Box Plot")
plt.savefig("graphs/Finance/Bill_Paid_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# #Savings
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Savings"])
plt.title("Savings Box Plot")
plt.savefig("graphs/Finance/Savings_boxplot.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


#####Bivariate analysis
#Income vs Savings
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Income",
    y="Savings",
    data=df
)
plt.title("Income vs Savings")
plt.savefig("graphs/Finance/Income_vs_Savings.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#Income vs Food
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Income",
    y="Food",
    data=df
)
plt.title("Income vs Food")
plt.savefig("graphs/Finance/Income_vs_Food.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#Income vs Shopping
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Income",
    y="Shopping",
    data=df
)
plt.title("Income vs Shopping")
plt.savefig("graphs/Finance/Income_vs_Shopping.png",
            dpi=300,
            bbox_inches="tight")
plt.show()


#Income vs Entertainment
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Income",
    y="Entertainment",
    data=df
)
plt.title("Income vs Entertainment")
plt.savefig("graphs/Finance/Income_vs_Entertainment.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#Income vs Transport
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Income",
    y="Transport",
    data=df
)
plt.title("Income vs Transport")
plt.savefig("graphs/Finance/Income_vs_Transport.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

######correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("graphs/Habit_Tracker/Correlation_Heatmap.png",
            dpi=300,
            bbox_inches="tight")
plt.show()