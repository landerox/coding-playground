"""Function to determine the resistance value from resistor color codes."""

from typing import List


def value(colors: List[str]) -> int:
    """Calculate the resistance value from the first two color bands.

    Args:
        colors (List[str]): A list of color names representing the resistor bands.

    Returns:
        int: The two-digit resistance value formed by the first two bands.

    """
    color_to_value = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    first_digit = color_to_value.get(colors[0].lower(), 0)
    second_digit = color_to_value.get(colors[1].lower(), 0)
    return first_digit * 10 + second_digit
