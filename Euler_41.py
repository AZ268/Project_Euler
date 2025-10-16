# Problem 41
# Pandigital Prime
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Generate all permutations of a string (recursive)
def get_permutations(s):
    if len(s) <= 1:
        return [s]
    perms = []
    for i in range(len(s)):
        c = s[i]
        rest = s[:i] + s[i+1:]
        for p in get_permutations(rest):
            perms.append(c + p)
    return perms

# Try pandigital numbers from 7 digits down to 1
def largest_pandigital_prime():
    for n in range(7, 0, -1):  # Try 7 to 1-digit pandigital numbers
        digits = ''.join(str(i) for i in range(n, 0, -1))  # e.g., '7654321'
        perms = get_permutations(digits)
        # Check permutations in descending numerical order
        nums = sorted([int(p) for p in perms], reverse=True)
        for num in nums:
            if is_prime(num):
                return num

# Run it
print("Largest pandigital prime:", largest_pandigital_prime())