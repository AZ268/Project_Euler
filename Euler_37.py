# Problem 37
# Truncatable Primes

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5 and 7 are not considered to be truncatable primes.

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

def is_truncatable(n):
    s = str(n)
    # Truncate left to right
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    # Truncate right to left
    for i in range(len(s)):
        if not is_prime(int(s[:len(s)-i])):
            return False
    return True

# Find the 11 truncatable primes
truncatable_primes = []
n = 11  # Start from 11, since 2, 3, 5, and 7 are excluded
while len(truncatable_primes) < 11:
    if is_prime(n) and is_truncatable(n):
        truncatable_primes.append(n)
    n += 2  # Only check odd numbers (even ones aren't prime except 2)

# Output result
print("Truncatable primes:", truncatable_primes)
print("Sum:", sum(truncatable_primes))