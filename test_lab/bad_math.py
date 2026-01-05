"""
Mathematical calculation utilities module.
"""


def calculate_sum(first_number, second_number):
    """
    Calculate the sum of two numbers.

    This function performs addition of two numeric values and returns
    the result without any side effects.

    Args:
        first_number (int | float): The first number to add
        second_number (int | float): The second number to add

    Returns:
        int | float: The sum of the two input numbers

    Examples:
        >>> calculate_sum(5, 3)
        8
        >>> calculate_sum(2.5, 1.5)
        4.0
    """
    return first_number + second_number
