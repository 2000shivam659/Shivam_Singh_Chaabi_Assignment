def compare_lists(list1, list2):
    """
    Compares two lists and returns the common elements (set intersection)
    and the non-common elements (set symmetric difference).

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        tuple: A tuple containing two lists -
        the common elements and the non-common elements.
    """
    # Find the common elements using set intersection
    common_elements = list(set(list1) & set(list2))

    # Find the non-common elements using set symmetric difference
    non_common_elements = list(set(list1) ^ set(list2))

    # Return the results as a tuple
    return common_elements, non_common_elements


# Prompt the user to enter mainstream list
print("Enter a list of items from mainstream and to end press enter only:")
mainstream = []
while True:
    item = input()
    if item == "":
        break
    mainstream.append(item)

# Prompt the user to enter must watch list
print("Enter a list of items from must watch and to end press enter only:")
must_watch = []
while True:
    item = input()
    if item == "":
        break
    must_watch.append(item)

# Call the compareLists function to get the common and non-common elements
common, non_common = compare_lists(mainstream, must_watch)

# Print the common elements
print("Common Elements:", common)

# Print the non-common elements
print("Non-Common Elements:", non_common)
