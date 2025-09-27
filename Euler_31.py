# Problem 31
# Coin Sums
# How many different ways can 2pounds be made using any number of coins?

def count_ways_recursive(amount, coins, index=0):
    if amount == 0:
        return 1  # Found a valid combination
    if amount < 0 or index == len(coins):
        return 0  # No valid combination

    # Two choices:
    # 1. Include the coin at current index
    # 2. Skip the coin and move to the next
    return (count_ways_recursive(amount - coins[index], coins, index) +
            count_ways_recursive(amount, coins, index + 1))

# Define the coins in pence
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

print(count_ways_recursive(target, coins))
