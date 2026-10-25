
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

# First subplot
plt.subplot(2, 1, 1)
plt.plot(x, y1, color='blue', marker='o', label='Data 1')
plt.title("Line Plot")
plt.legend()
plt.grid(True)

# Second subplot
plt.subplot(2, 1, 2)
plt.plot(x, y2, color='red', marker='s', label='Data 2')
plt.title("Second Line Plot")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
