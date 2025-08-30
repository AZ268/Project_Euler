# Problem 3
# Highly Divisible Triangular Number
# What is the value of the first triangle number to have over five hundred divisors?

import math

def count_divisors(n):
    count = 0
    sqrt_n = int(math.isqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2
    if sqrt_n * sqrt_n == n:
        count -= 1
    return count

def find_triangle_number(min_divisors):
    n = 1
    while True:
        triangle = n * (n + 1) // 2
        if count_divisors(triangle) > min_divisors:
            return triangle
        n += 1

# Find the first triangle number with over 500 divisors
result = find_triangle_number(500)
print(result)