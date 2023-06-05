def switch_dict(dict_input):
    """
    Switches the positions of keys and values in a dictionary.

    Args:
        dict_input (dict): The input dictionary.

    Returns:
        dict: A new dictionary with keys and values switched.
    """
    return {value: key for key, value in dict_input.items()}


# Prompt the user to enter key and value
print("Enter a dictionary item in the format 'k1:v1,k2:v2,...' ")
items = input()

input_dict = {}

for item in items.split(','):
    key, value = item.split(':')
    input_dict[key] = value

# Call the switch_dict function to switch the keys and values in the dictionary
result_dict = switch_dict(input_dict)

# Print the output dictionary with each key-value pair on a separate line
for key, value in result_dict.items():
    print(f"{key}: {value}")
