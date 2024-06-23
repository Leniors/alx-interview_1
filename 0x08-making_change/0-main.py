#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

#!/usr/bin/python3
"""
Task 0. Change comes from within

Determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """makeChange

    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    Arguments:
        coins (List): A list (pile) of coins of different values.
        total (int): The total needed.

    Return:
        (int): The minimum number of coins needed to meet the total.
    """
    temp_value = 0
    coins.sort(reverse=True)

    if total <= 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1