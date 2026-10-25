
import numpy as np

# Create arrays
a = np.array([1, 4, 9])
b = np.array([10, 20, 30])

# Vectorized addition
print("Addition:", np.add(a, b))

# Universal functions
print("Square Root:", np.sqrt(a))
print("Exponential:", np.round(np.exp(a), 2))

# Broadcasting
c = np.array([[1, 2, 3],
              [4, 5, 6]])
d = np.array([10, 20, 30])

print("Broadcasting Addition:\n", c + d)
print("Broadcasting Multiplication:\n", c * 2)
