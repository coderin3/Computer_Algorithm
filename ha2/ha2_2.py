def min_stamps(stamps, target):
    # Initialize DP table with infinity for all values (meaning "not yet reachable")
    dp = [float('inf')] * (target + 1)
    
    # Base case: 0 cents requires 0 stamps
    dp[0] = 0
    
    # Fill the DP table from 1 cent up to the target
    for i in range(1, target + 1):
        # Try every stamp denomination
        for stamp in stamps:
            # Only use this stamp if it doesn't exceed the current amount
            if stamp <= i:
                # If using this stamp gives a better (smaller) count, update dp[i]
                dp[i] = min(dp[i], dp[i - stamp] + 1)
    
    ### generated manually
    # Print the DP table header
    print(f"{'Target':>8} | {'Min Stamps':>10}")
    print("-" * 22)
    
    # Print each row: target amount and the minimum stamps needed to reach it
    for i in range(1, target + 1):
        # Show "N/A" if the amount is unreachable with the given stamp denominations
        val = dp[i] if dp[i] != float('inf') else "N/A"
        print(f"{i:>8} | {str(val):>10}")
    ###
    
    # Return the minimum number of stamps needed for the target amount
    return dp[target]

# Input Data: available stamp denominations (in cents)
stamp_values = [1, 10, 21, 34, 70, 100, 350, 1225, 1500]

# The target amount we want to reach (in cents)
target_value = 140

# Run the function and store the result
result = min_stamps(stamp_values, target_value)

# Print the final answer
print(f"\nMinimum stamps for {target_value} cents: {result}")