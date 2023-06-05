def merge(arr, l, m, r):
    """
    Merges two arrays: arr[l...m] and arr[m+1...r].

    Args:
        arr (list): The array to be merged.
        l (int): The starting index of the first subarray.
        m (int): The ending index of the first subarray.
        r (int): The ending index of the second subarray.
    """
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        arr (list): The array to be sorted.
        l (int): The starting index of the subarray to be sorted.
        r (int): The ending index of the subarray to be sorted.
    """
    if l < r:
        m = l + (r - l) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


# Prompt the user to enter the size of array
n = int(input("Enter the length of the array: "))

# Prompt the user to enter elements of array
arr = list(map(int, input("Enter the array elements: ").strip().split()[:n]))

# Print original array
print("Original Array:", arr)

# Call the function merge sort to sort the array
merge_sort(arr, 0, n - 1)

# Print the sorted array
print("Sorted Array:", arr)
