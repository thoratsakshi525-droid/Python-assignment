
import pandas as pd

# Create a Series
s = pd.Series([10, 20, 30, 40, 50])
print("Series:")
print(s)

# Create a DataFrame
data = {
    "Name": ["Amit", "Riya", "Raj", "Neha", "Pooja"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Display first and last rows
print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

# Statistical summary
print("\nDescription:")
print(df.describe())

# Export DataFrame to CSV
df.to_csv("students.csv", index=False)
print("\nData exported to CSV successfully.")

# Import CSV file
df2 = pd.read_csv("students.csv")
print("\nImported CSV Data:")
print(df2)

# Basic operations
print("\nTotal Marks:", df["Marks"].sum())
print("Average Marks:", df["Marks"].mean())
