A = [24, 75, 92, 83, 61, 48, 97, 50]


# Type 1: 2(n-1) comparisons
# Each element is compared twice: one for min, one for max
def find_max_min_type1(arr):
    comparisons = 0
    mn = mx = arr[0]  # initialize with first element (no comparison needed)

    for i in range(1, len(arr)):  # iterate n-1 times
        comparisons += 1
        if arr[i] < mn:  # comparison 1: min check
            mn = arr[i]

        comparisons += 1
        if arr[i] > mx: # comparison 2: max check
            mx = arr[i]

    return mn, mx, comparisons


# Type 2: floor(3n/2)-2 comparisons
# Split array in half recursively
# merge by comparing only the two candidates
def find_max_min_type2(arr, left, right):
    # Base case 1: single element is both min and max, 0 comparisons
    if left == right:
        return arr[left], arr[left], 0

    # Base case 2: two elements, 1 comparison determines min and max directly
    if right - left == 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right], 1 # left=min, right=max
        else:
            return arr[right], arr[left], 1 # right=min, left=max

    # Recursive case: split into left and right, solve each, then merge
    mid = (left + right) // 2
    mn_l, mx_l, cmp_l = find_max_min_type2(arr, left, mid)       # solve left half
    mn_r, mx_r, cmp_r = find_max_min_type2(arr, mid + 1, right)  # solve right half

    # Merge: 1 comparison for min, 1 for max = 2 comparisons at this level
    final_min = mn_l if mn_l < mn_r else mn_r
    final_max = mx_l if mx_l > mx_r else mx_r

    return final_min, final_max, cmp_l + cmp_r + 2  # accumulate total comparisons


# Run
print(f"Array: {A}  (n = {len(A)})\n")

mn, mx, cmp = find_max_min_type1(A)
print("Type 1")
print(f"  MIN = {mn}, MAX = {mx}")
print(f"  Comparisons: {cmp}  (expected 2n-2 = {2*(len(A)-1)})\n")

mn, mx, cmp = find_max_min_type2(A, 0, len(A) - 1)
print("Type 2")
print(f"  MIN = {mn}, MAX = {mx}")
print(f"  Comparisons: {cmp}  (expected floor(3n/2)-2 = {3*len(A)//2 - 2})")