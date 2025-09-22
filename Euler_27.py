# Euler 27
# Quadratic Primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

max_count = 0
product = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while is_prime(n * n + a * n + b):
            n += 1
        if n > max_count:
            max_count = n
            product = a * b

print "Product of a and b:", product