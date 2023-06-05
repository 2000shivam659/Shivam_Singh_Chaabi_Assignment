def get_sublist(lst, start_index, end_index):
    """
    Returns a sub-list from the given list,
    enclosed within the specified indices,
    containing every second element.

    Args:
        lst (list): The input list.
        start_index (int): The starting index of the sub-list (inclusive).
        end_index (int): The ending index of the sub-list (inclusive).

    Returns:
        list: The sub-list containing every second element.
    """
    sub_list = lst[start_index: end_index: 2]
    # print(sub_list)
    return sub_list


# Prompt the user to enter a list of elements
input_list = map(int, input("Enter the list elements: ").strip().split(' '))
input_list = list(input_list)

# Prompt the user to input starting index
start_index = int(input("Enter the starting index: "))

# Prompt the user to enter ending index
end_index = int(input("Enter the ending index: "))

# Call the get_sublist function to retrieve the desired sub-list
result = get_sublist(input_list, start_index, end_index)

# Print the result
print(result)
