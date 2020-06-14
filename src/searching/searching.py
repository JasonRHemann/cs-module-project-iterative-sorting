def linear_search(arr, target):
    # Your code here
    for index, value in enumerate(arr):
        if value == target:
            return index
            
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    mid = len(arr)//2
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1

    return -1  # not found
