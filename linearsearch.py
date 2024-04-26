def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
