# Problem 10
# Summation of Primes
# The sum of the primes below 10 is 2+3+5+7=17.
# Find the sum of all the primes below two million.

def true_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_primes(the_max_prime):
    return sum(n for n in range(2, the_max_prime) if true_prime(n))

# Find the sum of all primes below two million
result = sum_of_primes(2_000_000)
print(result)