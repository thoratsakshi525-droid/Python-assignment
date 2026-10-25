
import math

# Numeric data types
a = 10
b = 5.5
c = 2 + 3j

print("Integer:", a, type(a))
print("Float:", b, type(b))
print("Complex:", c, type(c))

# String
s = "Python"
print("String:", s)
print("Length:", len(s))
print("Uppercase:", s.upper())

# List
lst = [10, 20, 30]
lst.append(40)
print("List:", lst)

# Tuple
t = (1, 2, 3)
print("Tuple:", t)

# Dictionary
d = {"name": "Amit", "age": 20}
print("Dictionary:", d)
print("Name:", d["name"])

# Set
st = {1, 2, 3, 3}
print("Set:", st)

# Frozenset
fs = frozenset([1, 2, 3])
print("Frozenset:", fs)

# Boolean
flag = True
print("Boolean:", flag, type(flag))

# NoneType
x = None
print("NoneType:", x, type(x))

# Built-in functions
print("Absolute value:", abs(-10))
print("Maximum:", max(10, 20, 30))
print("Minimum:", min(10, 20, 30))
print("Sum:", sum(lst))
print("Rounded value:", round(5.678, 2))

# Math functions
print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Value of pi:", math.pi)
