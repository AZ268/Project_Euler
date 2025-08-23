# Problem 7
# By listing the first six prime numbers: 2,2,5,7,11 and 13, we can see that the 6th prime is 13.
# What is the 10001 prime number?

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_n_primes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

print(first_n_primes(10001))