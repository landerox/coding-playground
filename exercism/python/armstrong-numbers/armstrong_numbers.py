"""Function to determine if a given number is an Armstrong number."""


def is_armstrong_number(number: int) -> bool:
    """Check if a given number is an Armstrong number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.

    """
    digits = str(number)
    num_digits = len(digits)

    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)

    return armstrong_sum == number
