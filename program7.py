
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Line Plot
plt.plot(x, y, marker='o')
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Plot")
plt.show()

# Bar Plot
plt.bar(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Bar Plot")
plt.show()

# Scatter Plot
plt.scatter(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot")
plt.show()

# Histogram
marks = [40, 50, 60, 60, 70, 70, 70, 80, 90, 90]
plt.hist(marks, bins=5)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

