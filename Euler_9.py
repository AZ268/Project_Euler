# Problem 9
# Special Pythagorean Triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2+b^2=c^2.
# For example, 3^2+4^2= 9+16 =25 = 5^2
# There exists exactly one Pythagorean triplet for which a+b+c=1000.
# Find the product abc.

def special_pythagorean_triplet()-> int:
    for a in range (1,1000):
        for b in range(a, 500 - a // 2):
            c=1000-a-b
            if a**2+b**2==c**2:
                #print(a, b, c)
                #print(a+b+c)
                #print (a**2+b**2==c**2)
                return a*b*c

print(special_pythagorean_triplet())

