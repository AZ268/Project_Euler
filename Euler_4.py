# Problem 4
# Largest Palindrome Product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91x99.
# Find the largest palindrome made from the product of two 3-digit numbers.


palindrome_list=[]

for num_one in range (100, 1000):
    for num_two in range (100,1000):
        result = num_one * num_two
        if str(result) == str(result)[::-1]:
            palindrome_list.append(result)
            #break

print(palindrome_list)
print(max(palindrome_list))
