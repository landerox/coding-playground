"""Function to calculate the number of steps in the Collatz Conjecture."""


def steps(number: int) -> int:
    """Calculate the number of steps required to reach 1 in the Collatz Conjecture.

    The function takes a strictly positive integer and applies the Collatz
    Conjecture rules until the number becomes 1. If the input is zero or a
    negative integer, a ValueError is raised.

    Args:
        number (int): A strictly positive integer.

    Returns:
        int: The number of steps required to reach 1.

    Raises:
        ValueError: If the input number is zero or a negative integer.

    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps_count = 0

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        steps_count += 1

    return steps_count
