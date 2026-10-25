
import pandas as pd
import numpy as np

# Create DataFrame
data = {
    "Name": ["Amit", "Riya", "Raj", "Neha", "Pooja"],
    "Marks": [85, np.nan, 78, 90, np.nan],
    "Department": ["CS", "IT", "CS", "IT", "CS"]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull())

# Replace missing values
df["Marks"] = df["Marks"].fillna(0)
print("\nAfter Filling Missing Values:")
print(df)

# Drop rows with missing values
df2 = pd.DataFrame(data).dropna()
print("\nAfter Dropping Missing Values:")
print(df2)

# Replace data
df["Department"] = df["Department"].replace("CS", "Computer")
print("\nAfter Replacing Data:")
print(df)

# Filter rows
print("\nMarks Greater Than 80:")
print(df[df["Marks"] > 80])

# Sort values
print("\nSorted Data:")
print(df.sort_values(by="Marks", ascending=False))

# Group values
print("\nDepartment-wise Average Marks:")
print(df.groupby("Department")["Marks"].mean())
