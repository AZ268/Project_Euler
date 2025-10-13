# Problem 40
# Champernowne's Constant
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.12345678910111213141516...
# Let dn be the n-th digit of the fractional part. Find the value of the following expression:
# d1 x d10 x d100 x d1000 x d10000 x d100000


def champernowne_digit(position):
    length = 1
    count = 9
    start = 1

    while position > length * count:
        position -= length * count
        length += 1
        count *= 10
        start *= 10

    number = start + (position - 1) // length
    digit_index = (position - 1) % length
    return int(str(number)[digit_index])

def solve_euler_40():
    positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1
    for pos in positions:
        digit = champernowne_digit(pos)
        product *= digit
    return product

print(solve_euler_40())