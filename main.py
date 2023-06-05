from functools import reduce
from datetime import datetime, timedelta


class basics:
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


class dictionary_what:
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
    extension_type = input("Enter extension & type in form 'e1,t1;e2,t2;': ")

    # Prompt the user to enter the list of filenames
    file_list = input("Enter a list of filenames separated by space: ").split()

    # Call the function to get the file types
    result = get_file_type(extension_type, file_list)

    # Print the result
    print(result)


class column_sorting_yay:
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


class the_power_of_one_line:
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

    # Call the switch_dict function to switch the keys and values
    result_dict = switch_dict(input_dict)

    # Print the output dictionary with each key-value pair on a separate line
    for key, value in result_dict.items():
        print(f"{key}: {value}")


class common_not_common:
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


class every_other_suub_list:
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
    input_list = map(int, input("Enter list elements: ").strip().split(' '))
    input_list = list(input_list)

    # Prompt the user to input starting index
    start_index = int(input("Enter the starting index: "))

    # Prompt the user to enter ending index
    end_index = int(input("Enter the ending index: "))

    # Call the get_sublist function to retrieve the desired sub-list
    result = get_sublist(input_list, start_index, end_index)

    # Print the result
    print(result)


class fadctorial_of_a_number:
    def calculate_factorial(n):
        """
        Calculates the factorial of a number using a lambda function.

        Args:
            n (int): The number for which to calculate the factorial.

        Returns:
            int: The factorial of the given number.
        """
        factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
        return factorial(n)

    # Prompt the user to enter a number
    number = int(input("Enter a number: "))

    # Call the calculateFactorial function to find the factorial
    result = calculate_factorial(number)

    # Print the factorial of a given number
    print(f"The factorial of {number} is: {result}")


class something_neat_tricks_up_her_sleeve:
    # Looking at the below code, print down the final values of A0, A1, ...An

    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    print(A0)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    A1 = range(10)
    print(A1)  # range(0, 10)

    A2 = sorted([i for i in A1 if i in A0])
    print(A2)  # []

    A3 = sorted([A0[s] for s in A0])
    print(A3)  # [1, 2, 3, 4, 5]

    A4 = [i for i in A1 if i in A3]
    print(A4)  # [1, 2, 3, 4, 5]

    A5 = {i: i * i for i in A1}
    print(A5)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

    A6 = [[i, i * i] for i in A1]
    print(A6)  # [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

    A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])
    print(A7)  # 21

    A8 = map(lambda x: x * 2, [1, 2, 3, 4])
    print(A8)  # <map object at 0x000002BA481ABDC0>

    A9 = filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"])
    print(A9)  # <filter object at 0x000002728C6ABE20>


class difference_days:
    def check_date_difference(from_date, to_date, difference):
        """
        Check the difference between two dates with a specified number of days.

        Args:
            from_date (str): The starting date in the form 'yy-mm-dd'.
            to_date (str): The ending date in the form 'yy-mm-dd'.
            difference (int): The number of days used for comparison.

        Returns:
            bool: True if the difference between the dates < difference
            else False otherwise.
        """
        # Convert the date strings to datetime objects
        from_date_time = datetime.strptime(from_date, '%y-%m-%d')
        to_date_time = datetime.strptime(to_date, '%y-%m-%d')

        # Calculate the difference between the dates
        date_difference = to_date_time - from_date_time

        # Compare the difference with the specified number of days
        if date_difference < timedelta(days=difference):
            return True
        else:
            return False

    # Prompt the user to enter from date
    from_date = input("Enter the from date in the form of 'yy-mm-dd': ")

    # Prompt the user to enter to date
    to_date = input("Enter the to date in the form of 'yy-mm-dd': ")

    # Prompt the user to enter difference
    difference = int(input("Enter the difference: "))

    # Call the function check_date_difference and print the output
    result = check_date_difference(from_date, to_date, difference)
    print(result)


class of_date_and_days:
    def get_previous_date(date, n):
        """
        Returns the string representation of date n days before the given date.

        Args:
            date (str): The date in the format 'yy-mm-dd'.
            n (int): The number of days.

        Returns:
            str: The string representation of the previous date.
        """
        # Convert the date string to a datetime object
        current_date = datetime.strptime(date, '%y-%m-%d')

        # Calculate the previous date by subtracting n days
        previous_date = current_date - timedelta(days=n)

        # Format the previous date as a string in 'yy-mm-dd' format
        previous_date_str = previous_date.strftime('%y-%m-%d')

        return previous_date_str

    # Prompt the user to enter date
    date = input("Enter the date in form of 'yy-mm-dd': ")

    # Prompt the user to enter n i.e., number days to decrease
    n = int(input("Enter the number of days to decrease: "))

    # Call the function get_previous_date to increase n days
    previous_date = get_previous_date(date, n)

    # Print the day after n days
    print(f"The date {n} days before {date} is: {previous_date}")


class something_fishy:
    # Find output of following:

    def f(x, l=[]):
        for i in range(x):
            l.append(i * i)
        print(l)

    f(2)  # [0, 1]

    f(3, [3, 2, 1])  # [3, 2, 1, 0, 1, 4]

    f(3)  # [0, 1, 0, 1, 4]
