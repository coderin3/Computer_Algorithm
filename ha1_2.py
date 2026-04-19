def minimize_stamps(target_cost, denominations):
    # Total number of stamps used
    count = 0
    
    # Dictionary to store how many of each stamp is used
    # Key: stamp value, Value: number of stamps used
    used_stamps = {}
    
    # Iterate through each stamp denomination (assumed to be sorted in descending order)
    for stamp in denominations:
        if target_cost == 0: # If no cost remains, stop early (optimization)
            break
        
        # Calculate how many stamps of this value fit into the remaining cost
        num_stamps = target_cost // stamp
        
        if num_stamps > 0: # If at least one stamp can be used
            count += num_stamps # Add to total count
            used_stamps[stamp] = num_stamps # Record usage in dictionary
            # Update the remaining cost
            target_cost %= stamp
            
    return count, used_stamps # Return total number of stamps and detailed breakdown

# Input Data
cost = 140
stamps = [1500, 1225, 350, 100, 70, 34, 21, 10, 1]

# Execution
total_count, breakdown = minimize_stamps(cost, stamps)

print(f"Total stamps needed: {total_count}")
print("Breakdown of stamps used:")
for val, qty in breakdown.items():
    print(f"- {qty} stamp(s) of {val} cents")