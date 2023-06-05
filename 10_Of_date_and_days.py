from datetime import datetime, timedelta


def get_previous_date(date, n):
    """
    Returns the string representation of a date n days before the given date.

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
