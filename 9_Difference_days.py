from datetime import datetime, timedelta


def check_date_difference(from_date, to_date, difference):
    """
    Checks if the difference between two dates with a specified number of days.

    Args:
        from_date (str): The starting date in the form 'yy-mm-dd'.
        to_date (str): The ending date in the form 'yy-mm-dd'.
        difference (int): The number of days used for comparison.

    Returns:
        bool: True if the difference between the dates is less than difference
        False otherwise.
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
