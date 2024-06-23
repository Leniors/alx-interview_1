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
    if total <= 0:
        return 0
    
    # Initialize DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: No coins needed to make 0
    
    # Populate the DP array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still inf, it means we cannot make the amount total
    return dp[total] if dp[total] != float('inf') else -1
