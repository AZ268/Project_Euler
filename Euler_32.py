# Problem 32
# Pandigital Products

def is_pandigital(a, b, c):
    s = str(a) + str(b) + str(c)
    if len(s) != 9:
        return False
    return set(s) == set("123456789")

def euler_32():
    products = set()
    for a in range(1, 100):  # a can be 1-2 digits
        for b in range(100, 5000):  # b can be 3-4 digits
            c = a * b
            if is_pandigital(a, b, c):
                products.add(c)
    return sum(products)

print(euler_32())