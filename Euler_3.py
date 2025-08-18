#Problem 3
#Largest Prime Factor
# The prime factors of 13195 are 5,7,13 and 29
# What is the largest prime factor of the number 600851475143?


prime_factors=[]
my_number= 600851475143
factor=2


while my_number > 1:
    if my_number % factor == 0:
        prime_factors.append(factor)
        my_number /= factor
        #print(factor)
    else:
        factor += 1

print(max(prime_factors))