# Problem 35
# Circular Primes
# The number,197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719 are themselves prime.
#How many circular primes are there below one million?

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def circular_primes(limit):
    primes = set()
    for i in range(2, limit):
        if is_prime(i):
            primes.add(i)

    count = 0
    for p in primes:
        if all(rot in primes for rot in rotations(p)):
            count += 1
    return count

# Run the function for limit = 1,000,000
print(circular_primes(1000000))