
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create dataset
df = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5],
    "Marks": [50, 60, 70, 80, 90],
    "Study_Hours": [2, 3, 4, 5, 6],
    "Subject": ["A", "B", "A", "B", "A"]
})

# Line plot
sns.lineplot(x="Day", y="Marks", data=df)
plt.title("Line Plot")
plt.show()

# Bar plot
sns.barplot(x="Subject", y="Marks", data=df)
plt.title("Bar Plot")
plt.show()

# Histogram
sns.histplot(data=df, x="Marks", bins=5)
plt.title("Histogram")
plt.show()

# Box plot
sns.boxplot(data=df, y="Marks")
plt.title("Box Plot")
plt.show()

# Scatter plot
sns.scatterplot(x="Study_Hours", y="Marks", data=df)
plt.title("Scatter Plot")
plt.show()
