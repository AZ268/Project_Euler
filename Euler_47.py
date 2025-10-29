# Problem 47
# Distinct Primes Factors
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

def count_distinct_prime_factors(n):
    count = 0
    factor = 2
    while n > 1:
        if n % factor == 0:
            count += 1
            while n % factor == 0:
                n //= factor
        factor += 1
        if factor * factor > n:
            if n > 1:
                count += 1
            break
    return count


def find_consecutive_numbers(target_factors, consecutive):
    n = 2
    streak = 0
    while True:
        if count_distinct_prime_factors(n) == target_factors:
            streak += 1
            if streak == consecutive:
                return n - consecutive + 1
        else:
            streak = 0
        n += 1


# Euler 47: four distinct prime factors, four consecutive numbers
result = find_consecutive_numbers(4, 4)
print(result)