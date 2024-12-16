"""Function to classify positive integers as perfect, abundant, or deficient."""


def aliquot_sum(number: int) -> int:
    """Calculate the aliquot sum of a given number.

    The aliquot sum is the sum of the divisors of a number, excluding the number itself.

    Args:
        number (int): A positive integer.

    Returns:
        int: The aliquot sum of the input number.

    """
    return sum(
        divisor for divisor in range(1, number // 2 + 1) if number % divisor == 0
    )


def classify(number: int) -> str:
    """Classify a positive integer as perfect, abundant, or deficient.

    The classification is based on the aliquot sum of the number:
    - Perfect: The number equals its aliquot sum.
    - Abundant: The number is less than its aliquot sum.
    - Deficient: The number is greater than its aliquot sum.

    Args:
        number (int): A positive integer to classify.

    Returns:
        str: The classification of the input integer ("perfect", "abundant",
             or "deficient").

    Raises:
        ValueError: If the input number is not a positive integer.

    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    sum_of_factors = aliquot_sum(number)

    if sum_of_factors == number:
        return "perfect"
    elif sum_of_factors > number:
        return "abundant"
    else:
        return "deficient"
