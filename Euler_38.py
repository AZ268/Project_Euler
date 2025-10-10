# Problem 38
# Pandigital Multiples
# Find the largest 1 to 9 pandigital number that can be formed as the concatenated product of an integer
# with (1,2, ... , n) where n > 1.

def is_pandigital(s):
    return len(s) == 9 and set(s) == set('123456789')


def find_largest_pandigital_multiple():
    max_pandigital = 0

    # Try numbers from 1 up to 9999
    # Why 9999? Because if num has 5 digits, even num*1 is already >9 digits when concatenated
    for num in range(1, 10000):
        concatenated = ''
        n = 1
        while len(concatenated) < 9:
            concatenated += str(num * n)
            n += 1
        if is_pandigital(concatenated):
            max_pandigital = max(max_pandigital, int(concatenated))

    return max_pandigital


print(find_largest_pandigital_multiple())