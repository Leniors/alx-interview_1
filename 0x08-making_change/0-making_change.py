#!/usr/bin/python3
"""
makeChangee file
"""
def makeChange(coins, total):
    """ makeChange function
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
