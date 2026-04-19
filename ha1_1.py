import random

# Global counters for algorithm analysis
comparison_count = 0 # Total number of element comparisons
recursive_count  = 0 # Total number of recursive calls

def optimized_quick_sort(arr):
    global comparison_count, recursive_count
        
    # Count every function call (including base cases)
    recursive_count += 1
    
    # Base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Random pivot → breaks adversarial patterns
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
        
    # Three-way partitioning
    less, equal, greater = [], [], []
    
    ### 
    # ### means a part that I refactored manually
    for x in arr:
        comparison_count += 1
        if x < pivot:    less.append(x) # elements smaller than pivot
        elif x == pivot: equal.append(x) # elements equal to pivot
        else:            greater.append(x) # elements larger than pivot
        
        # Since add return value in less, equal, greater order, 
        # I changed if-else order to less -> equal -> greater.

    return  optimized_quick_sort(less) + equal +  optimized_quick_sort(greater)
    ###
    
# run 
adversarial_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted_array = optimized_quick_sort(adversarial_array)

### 
# ### means a part where I refactored manually
# I modified output part to adjust the same format as first one
print(f"Original: {adversarial_array}")
print(f"Sorted:   {sorted_array}")
print(f"Total Function Calls:      {recursive_count}")
print(f"Total Comparison Counts:   {comparison_count}")
###