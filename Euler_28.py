# Problem 28
# Number Spiral Diagonals
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Each time the corners are n², n² - (n-1), n² - 2(n-1), n² - 3(n-1)
def spiral_diagonals_sum(size):
    total = 1  # Start with center
    for n in range(3, size + 1, 2):
        total += 4 * n * n - 6 * (n - 1)
    return total

print(spiral_diagonals_sum(1001))