#Solution to Euler nr.1 (2025)

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

"""Module"""
a=0
i=3
j=5

three_list= [3]
five_list= [5]

def my_function(idx, x, temp_list):
    try:
        while temp_list[idx] < 1000:
            if (temp_list[idx]) + x < 1000:
                temp_list.append((temp_list[idx]) + x)
            idx += 1
    except IndexError:
        print("fin")

my_function(a, i, three_list)
my_function(a, j, five_list)

print(three_list)
print(five_list)

res = list(set(three_list + five_list))
print(res)
print(sum(res))
