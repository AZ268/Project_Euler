# Problem 43
# Sub-string Divisibility
# Project Euler Problem 43 asks for the sum of all 0-9 pandigital numbers
# (numbers that use each digit 0-9 exactly once)
# that satisfy a special sub-string divisibility property.

def next_permutation(seq):
    """Generate the next lexicographical permutation in-place."""
    # Find the largest index i such that seq[i] < seq[i + 1]
    i = len(seq) - 2
    while i >= 0 and seq[i] >= seq[i + 1]:
        i -= 1
    if i == -1:
        return False  # last permutation reached

    # Find the largest index j > i such that seq[j] > seq[i]
    j = len(seq) - 1
    while seq[j] <= seq[i]:
        j -= 1

    # Swap
    seq[i], seq[j] = seq[j], seq[i]

    # Reverse the tail
    seq[i + 1:] = reversed(seq[i + 1:])
    return True


def to_int(digits, start, end):
    """Convert digits[start:end+1] to integer."""
    n = 0
    for i in range(start, end + 1):
        n = n * 10 + digits[i]
    return n


def has_property(d):
    """Check the divisibility property."""
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7):
        if to_int(d, i + 1, i + 3) % primes[i] != 0:
            return False
    return True


def euler43():
    digits = list(range(10))
    total = 0

    while True:
        if has_property(digits):
            num = 0
            for d in digits:
                num = num * 10 + d
            total += num

        if not next_permutation(digits):
            break

    return total


print(euler43())
