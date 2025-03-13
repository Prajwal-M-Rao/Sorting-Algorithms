def merge_sort(arr):
    """
    Function to perform Merge Sort on a given array.
    Uses a divide-and-conquer approach to recursively sort and merge subarrays.
    """
    if len(arr) <= 1:
        return arr  # Base case: A single-element array is already sorted

    # Step 1: Find the middle index
    mid = len(arr) // 2
    
    # Step 2: Recursively sort the left and right halves
    left_half = merge_sort(arr[:mid])  # Sorting the left half
    right_half = merge_sort(arr[mid:])  # Sorting the right half
    
    # Step 3: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Function to merge two sorted subarrays into a single sorted array.
    """
    sorted_arr = []  # List to store merged and sorted elements
    i = j = 0  # Pointers for left and right subarrays
    
    # Step 4: Compare elements from both subarrays and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # If left element is smaller, add it to sorted_arr
            sorted_arr.append(left[i])
            i += 1
        else:  # If right element is smaller, add it to sorted_arr
            sorted_arr.append(right[j])
            j += 1
    
    # Step 5: Append any remaining elements from left or right subarray
    sorted_arr.extend(left[i:])  # Add remaining elements from left (if any)
    sorted_arr.extend(right[j:])  # Add remaining elements from right (if any)
    
    return sorted_arr  # Return the final merged sorted array

# Example usage
arr = [8, 3, 7, 4, 9, 2, 6, 5]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]
