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
