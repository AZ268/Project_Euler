# Problem 36
# Double-base Palindromes
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def is_palindrome(s):
    return s == s[::-1]

def double_base_palindromes(limit):
    total = 0
    for n in range(1, limit):
        if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
            total += n
    return total

# Solve for numbers less than 1 million
result = double_base_palindromes(1000000)
print("Sum of double-base palindromes under 1 million:", result)