"""Functions to convert numbers into their corresponding raindrop sounds."""


def convert(number: int) -> str:
    """Convert a number to its corresponding raindrop sounds.

    Checks divisibility of the input number by 3, 5, and 7 to produce specific sounds.
    Returns the number as a string if no conditions are met.

    Args:
        number (int): The number to be converted.

    Returns:
        str: The corresponding raindrop sound or the number as a string.

    """
    result: str = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    return result if result else str(number)
