def quick_sort(arr):
    if len(arr) <= 1:  # Base case: If the array has 0 or 1 elements, it's already sorted
        return arr  

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = []   # Elements smaller than pivot
    middle = [] # Elements equal to pivot
    right = []  # Elements greater than pivot

    # Divide elements into left, middle, and right based on pivot
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)

    # Recursively sort the left and right parts, then combine
    return quick_sort(left) + middle + quick_sort(right)  

# Example usage
arr = [9, 3, 7, 5, 6, 8, 2, 4]
print("Sorted array:", quick_sort(arr))


# Optimised Code 
'''def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sorting

# Example usage
arr = [9, 3, 7, 5, 6, 8, 2, 4]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

'''