# Problem 6
# Sum Square Difference
# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385.
# The square of the sum of the first ten natural numbers is, (1+2+..+10)^2=3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025-385=2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import math
my_numbers=[]
my_numbers_squared=[]

for my_num in range (1,101):
    my_numbers.append(my_num)

for my_nums in range (1,101):
    my_numbers_squared.append(my_nums ** 2)

sum_of_my_numbers_squared = sum(my_numbers_squared)

#print (my_numbers)
sum_of_my_numbers = sum(my_numbers)
square_of_the_sum= sum_of_my_numbers**2
#print (sum_of_my_numbers)
result_difference = square_of_the_sum - sum_of_my_numbers_squared
print (result_difference)
