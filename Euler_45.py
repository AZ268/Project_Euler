# Problem 45
# Triangular, Pentagonal, and Hexagonal
# Find the next triangle number that is also pentagonal and hexagonal after 40,755.

def is_pentagonal(x):
    # Inverse of pentagonal formula P_n = n(3n-1)/2
    n = (1 + (1 + 24*x)**0.5) / 6
    return n.is_integer()

n = 144  # start after H_143 = 40755
while True:
    h = n * (2*n - 1)
    if is_pentagonal(h):
        print(h)
        break
    n += 1