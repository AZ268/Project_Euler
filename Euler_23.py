# Problem 23
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def get_divisors_sum(n):
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def is_abundant(n):
    return get_divisors_sum(n) > n

# Step 1: Get all abundant numbers up to 28123
abundant_numbers = [i for i in range(12, 28124) if is_abundant(i)]

# Step 2: Create a set of all numbers that are the sum of two abundant numbers
abundant_sums = set()
for i in abundant_numbers:
    for j in abundant_numbers:
        s = i + j
        if s <= 28123:
            abundant_sums.add(s)
        else:
            break

# Step 3: Sum of all numbers which are NOT in abundant_sums
non_abundant_sum = sum(i for i in range(1, 28124) if i not in abundant_sums)

print(non_abundant_sum)