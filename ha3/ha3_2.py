node_count = 0
prune_count = 0

def subset_sum(weights, target):
    global node_count, prune_count
    node_count = 0
    prune_count = 0

    ### generated manually
    weights.sort() # sort the weights in ascending order 
    # Crucial for the bounding condition (wsum + weights[index] > target) to prune efficiently.
    solutions = []
    
    # wsum: sum of the elements selected so far
    # rsum: sum of the remaining elements after the current index
    total = sum(weights) # total: total sum of all elements (used as the initial 'rsum')

    # divide subset_sum into is_expand and backtrack 
    # Bounding function
    def is_expand(index, wsum, rsum):
        # Condition 1: wsum + rsum >= M
        # Even if all remaining values are added, the sum is still less than the target -> stop searching
        condition1 = (wsum + rsum >= target)
        
        # Condition 2: wsum + w[i+1] <= M 
        # Adding the next element exceeds the target -> stop searching
        condition2 = (index < len(weights) and wsum + weights[index] <= target)
        return condition1 and condition2
	###
 
    def backtrack(index, wsum, rsum, subset): 
        global node_count, prune_count
        # count every recursive call as a visited node in the State Space Tree
        node_count += 1

        # base case: reached target sum accurately
        if wsum == target: ### changed name current_sum -> wsum
            solutions.append(list(subset))
            return
        
        # Reached the end of the weights => No more elements to explore
        if index >= len(weights):
            return    
		
        ### generated manually
		# Check is_expand: determine whether further exploration is worthwhile or should be pruned based on bounding conditions
        if not is_expand(index, wsum, rsum):
            prune_count += 1 # Count the branch as pruned
            return
        ###
        
		# Left Child Node: Include the current element (weights[index])  		
        subset.append(weights[index])     
        backtrack(index + 1, wsum + weights[index], rsum - weights[index], subset) # Update wsum (increases) and rsum (decreases) by selected weights


        # right node: Exclude the current element (weights[index])
        subset.pop()
        backtrack(index + 1, wsum, rsum - weights[index], subset) # wsum stays the same, rsum decreases (by passed weights)

		# Start backtracking from index 0, current sum 0, remaining sum 'total', and an empty subset
    backtrack(0, 0, total, [])
    return solutions

# Input Data
weights = [3, 34, 4, 12, 5, 2]
target = 9

solutions = subset_sum(weights, target)

print(f"Given weights: {weights}")
print(f"Target sum (M): {target}\n")
print(f"Found {len(solutions)} solution(s):")
for s in solutions:
    print(s)
    
print(f"Nodes visited : {node_count}")
print(f"Branches pruned: {prune_count}")