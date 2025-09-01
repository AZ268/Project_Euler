# Problem 14
# Longest Collatz Sequence
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def find_longest_collatz(limit):
    max_length = 0
    starting_number = 0

    for i in range(1, limit):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            starting_number = i

    return starting_number

# Run the function
print("The result is:", find_longest_collatz(1_000_000))
