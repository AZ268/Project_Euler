# Problem 20
# Factorial Digit
# n! means nx(n-1)x...x3x2x1
# For example 10!= 10x9x...x3x2x1=3628800 and the sum of the digits in the number
# is 10!=3+6+2+8+8+0+0= 27.
# Find the sum of the digits in the number 100!.

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_of_digits_in_factorial(n):
    fact = factorial(n)
    return sum(int(digit) for digit in str(fact))

print(sum_of_digits_in_factorial(100))
