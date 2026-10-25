
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load real-world dataset
df = sns.load_dataset("tips")

# Display dataset
print("First 5 Rows:")
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df = df.dropna()

# Line plot
sns.lineplot(x="size", y="total_bill", data=df)
plt.title("Total Bill by Group Size")
plt.show()

# Histogram
sns.histplot(data=df, x="total_bill")
plt.title("Distribution of Total Bills")
plt.show()

# Scatter plot
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Total Bill vs Tip")
plt.show()

# Correlation matrix
corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
