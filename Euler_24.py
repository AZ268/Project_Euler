# Problem 24
# Lexicographic Permutations
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def get_lexicographic_permutation(digits, position):
    position -= 1  # Convert to 0-based index
    result = []
    while digits:
        n = len(digits)
        f = factorial(n - 1)
        index = position // f
        result.append(digits.pop(index))
        position %= f
    return ''.join(result)

digits = list('0123456789')
position = 1000000

answer = get_lexicographic_permutation(digits, position)
print(answer)


#def factorial(n):
#    result = 1
#   for i in range(2, n + 1):
#       result *= i
#   return result

#digits = ['0','1','2','3','4','5','6','7','8','9']
#position = 1000000 - 1  # zero-based index
#answer = ''

#while digits:
#    n = len(digits)
#    f = factorial(n - 1)
#    index = position // f
#    answer += digits.pop(index)
#    position = position % f

#print(answer)