
import numpy as np

# Create 1D array
a = np.array([10, 20, 30, 40, 50])
print("1D Array:", a)

# Create array using arange()
b = np.arange(1, 11)
print("Arange Array:", b)

# Create array using linspace()
c = np.linspace(0, 10, 5)
print("Linspace Array:", c)

# Indexing
print("Element at index 2:", a[2])

# Slicing
print("Sliced Array:", a[1:4])

# Create 2D array
d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", d)

# Reshaping
e = np.reshape(b, (2, 5))
print("Reshaped Array:\n", e)

# Mathematical operations
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Addition:", a + 5)
print("Multiplication:", a * 2)
