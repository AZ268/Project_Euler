# Problem 15

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly
#  routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def routes(grid_size):
    numerator = factorial(2 * grid_size)
    denominator = factorial(grid_size) * factorial(grid_size)
    return numerator // denominator

# 20x20 grid
print("Number of routes:", routes(20))