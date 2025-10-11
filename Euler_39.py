# Problem 39
# Integer Right Triangles

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# For which value of p <= 1000, is the number of solutions maximised?

def count_solutions(p):
    count = 0
    for a in range(1, p // 3):
        for b in range(a, (p - a) // 2):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count

max_solutions = 0
result = 0

for p in range(1, 1001):
    solutions = count_solutions(p)
    if solutions > max_solutions:
        max_solutions = solutions
        result = p

print("Perimeter with max solutions:", result)