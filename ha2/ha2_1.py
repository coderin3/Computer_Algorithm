### generated binary_search function manually

# Binary search to find the leftmost position where target can be inserted
# to maintain sorted order in tails array
def binary_search(tails, target):
    left, right = 0, len(tails) - 1
    while left <= right:
        mid = (left + right) // 2
        if tails[mid] < target:
            left = mid + 1  # target is larger, search right half
        else:
            right = mid - 1 # target is smaller or equal, search left half
    return left # return insertion position
###

def find_lis_optimized(arr):
    n = len(arr)
    if n == 0:
        return 0, []
    ### generated manually
    tails = [] # stores the smallest tail element for each LIS length
    indices = [] # stores the actual arr index corresponding to each tails entry
    parent = [-1] * n # parent[i] = index of previous element in LIS ending at i

    for i, num in enumerate(arr):
        pos = binary_search(tails, num)  # binary search로 nested loop 대체

        if pos == len(tails):
        # num is larger than all tails → extends the longest subsequence
            tails.append(num)
            indices.append(i)
        else:
        # num replaces an existing tail → keeps tails values as small as possible
            tails[pos] = num
            indices[pos] = i

				# link current element to the previous element in the LIS
        if pos > 0:
            parent[i] = indices[pos - 1]
	 ###
	 
    max_len = len(tails) # length of LIS = number of entries in tails (no need for max())
    current_idx = indices[-1] # the last entry in indices always points to the end of the longest subsequence
    sequence = [] # backtrack through parent pointers to reconstruct the actual LIS
    while current_idx != -1:
        sequence.append(arr[current_idx])
        current_idx = parent[current_idx] 

    return max_len, sequence[::-1]  # sequence is built in reverse order, so flip it

nums = [10, 22, 9, 33, 21, 50, 41, 60]
lis_length, lis_sequence = find_lis_optimized(nums)
print(f"Input Array: {nums}")
print(f"Longest Increasing Subsequence: {lis_sequence}")
print(f"Length of LIS: {lis_length}")