def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_idx = i
        # Find the actual minimum in the rest of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = [7, 2, 9, 1, 6, 4, 10, 3, 8, 5]
selection_sort(arr)
print("Sorted array is:", arr)
