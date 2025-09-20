# Problem 26
# Reciprocal Cycles

def recurring_cycle_length(d):
    remainders = {}
    value = 1
    position = 0

    while value != 0:
        if value in remainders:
            return position - remainders[value]
        remainders[value] = position
        value = (value * 10) % d
        position += 1

    return 0  # terminates, no cycle

def find_longest_cycle(limit):
    max_length = 0
    result = 0

    for d in range(2, limit):
        length = recurring_cycle_length(d)
        if length > max_length:
            max_length = length
            result = d

    return result

print(find_longest_cycle(1000))