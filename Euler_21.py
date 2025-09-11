# Problem 21
# Amicable Numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# Evaluate the sum of all the amicable numbers under 10000.

def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def find_amicable_numbers(limit):
    amicable_sum = 0
    for a in range(2, limit):
        b = sum_of_divisors(a)
        if b != a and sum_of_divisors(b) == a:
            amicable_sum += a
    return amicable_sum

print(find_amicable_numbers(10000))
