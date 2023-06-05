def sort_list_dicts(list_of_dicts, sort_key):
    """
    Sorts a list of dictionaries based on a specified key.

    Args:
        list_of_dicts (list): List of dictionaries to be sorted.
        sort_key (str): Key based on which the list should be sorted.

    Returns:
        list: Sorted list of dictionaries.
    """
    sorted_list = sorted(list_of_dicts, key=lambda x: x[sort_key])
    return sorted_list


# Prompt the user to enter the input list of dictionaries
input_list = []
while True:
    item = input("Enter a dictionary item in the format 'k1:v1,k2:v2': ")
    if item == "":
        break
    input_dict = {}
    for pair in item.split(","):
        key, value = pair.split(':')
        input_dict[key] = value
    input_list.append(input_dict)

# Prompt the user to enter the sort key
sort_key = input("Enter the key to sort the list of dicts: ")

# Sort the list_of_Dictionaries based on the sort key
sorted_list = sort_list_dicts(input_list, sort_key)

# Print the dictionary on a separate line
for item in sorted_list:
    print(item)
