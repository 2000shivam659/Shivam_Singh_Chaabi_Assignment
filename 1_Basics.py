def sort_array(arr):
    """
    Sorts an array using the sort() method in ascending order.

    Args:
        arr (list): The array to be sorted.
    """
    return sorted(arr)


# Prompt the user to enter elements of array
arr = map(int, input("Enter the list elements: ").strip().split(' '))
arr = list(arr)

# Print original array
print("Original Array:", arr)

# Call the function merge sort to sort the array
arr = sort_array(arr)

# Print the sorted array
print("Sorted Array:", arr)
