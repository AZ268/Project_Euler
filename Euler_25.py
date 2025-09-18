# Problem 25
# 1000-digit Fibonacci Number
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

a, b = 1, 1
index = 2

while len(str(b)) < 1000:
    a, b = b, a + b
    index += 1

print(index)