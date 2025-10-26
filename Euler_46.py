# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum
# of a prime and twice a square.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def can_be_written(n):
    # Check if n = prime + 2*square
    for p in range(2, n):
        if is_prime(p):
            remainder = n - p
            if remainder % 2 == 0:
                k2 = remainder // 2
                k = int(k2**0.5)
                if k * k == k2:
                    return True
    return False

# Find the smallest odd composite that fails the conjecture
n = 9
while True:
    if not is_prime(n):
        if not can_be_written(n):
            print(n)
            break
    n += 2  # next odd number