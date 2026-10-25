
import numpy as np

# Generate random numbers
print("Random Numbers:", np.random.rand(5))

# Generate standard normal numbers
print("Normal Random Numbers:", np.random.randn(5))

# Generate random integers
print("Random Integers:", np.random.randint(1, 100, 5))

# Generate numbers from normal distribution
data = np.random.normal(50, 10, 5)
print("Normal Distribution:", np.round(data, 2))

# Calculate statistics
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
