def get_file_type(extension_type, file_list):
    """
    Find the type of file from extension type list.

    Args:
        extension_type: The string of containing extension with it's type.
        file_list: The string of containing file of different types.

    Returns:
        list: dictionary containing file with it's type of file.
    """
    file_types = {}

    # Create a dictionary of extension:type pairs
    extension_type_dict = {}
    for pair in extension_type.split(';'):
        extension, file_type = pair.split(',')
        extension_type_dict[extension] = file_type.strip()

    # Process each file in the file list
    for file in file_list:
        file_parts = file.split('.')
        extension = file_parts[-1].strip()
        if extension in extension_type_dict:
            file_types[file] = extension_type_dict[extension]
        else:
            file_types[file] = "unknown"

    return file_types


# Prompt the user to enter the extension:type pairs
extension_type = input("Enter extension & type in the form 'e1,t1;e2,t2;': ")

# Prompt the user to enter the list of filenames
file_list = input("Enter a list of filenames separated by space: ").split()

# Call the function to get the file types
result = get_file_type(extension_type, file_list)

# Print the result
print(result)
