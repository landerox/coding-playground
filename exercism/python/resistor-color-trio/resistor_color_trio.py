"""Function to calculate the resistance value of a resistor based on color codes."""

from typing import List

COLOR_CODES = {
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


def label(colors: List[str]) -> str:
    """Calculate the resistance value based on the color codes provided.

    Args:
        colors (List[str]): A list of color names as strings.

    Returns:
        str: The resistance value formatted as a string with units.

    """
    if len(colors) < 3:
        raise ValueError("At least three colors must be provided.")

    colors = colors[:3]

    try:
        first_digit = COLOR_CODES[colors[0].lower()]
        second_digit = COLOR_CODES[colors[1].lower()]
        multiplier = COLOR_CODES[colors[2].lower()]
    except KeyError as e:
        raise ValueError(f"Invalid color provided: {e}") from e

    base_value = first_digit * 10 + second_digit
    resistance_value = base_value * (10**multiplier)

    if resistance_value >= 1_000_000_000:
        formatted_value = f"{resistance_value // 1_000_000_000} gigaohms"
    elif resistance_value >= 1_000_000:
        formatted_value = f"{resistance_value // 1_000_000} megaohms"
    elif resistance_value >= 1_000:
        formatted_value = f"{resistance_value // 1_000} kiloohms"
    else:
        formatted_value = f"{resistance_value} ohms"

    return formatted_value
