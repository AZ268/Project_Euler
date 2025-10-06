# Problem 34
# Digit Factorials
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.


import math

factorials = {str(i): math.factorial(i) for i in range(10)}

def is_curious(n):
    return n == sum(factorials[d] for d in str(n))

# 1! and 2! are excluded as per problem statement
result = sum(n for n in range(10, 7 * factorials['9']) if is_curious(n))

print("Sum of all curious numbers:", result)