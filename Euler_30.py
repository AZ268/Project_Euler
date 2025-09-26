# Problem 30
# Digit Fifth Powers
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def digit_fifth_powers():
    return sum(
        n for n in range(10, 354295)
        if n == sum(int(d)**5 for d in str(n))
    )

print(digit_fifth_powers())