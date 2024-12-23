"""Functions to decode resistor color bands and list available colors."""

from typing import List


def color_code(color: str) -> int:
    """Get the numerical value associated with a resistor color band.

    Args:
        color (str): The color of the resistor band.

    Returns:
        int: The numerical value corresponding to the given color.

    """
    resistor_colors: List[str] = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    if color not in resistor_colors:
        raise ValueError(f"Invalid color: {color}.")
    return resistor_colors.index(color)


def colors() -> List[str]:
    """List all the available resistor color bands.

    Returns:
        List[str]: A list of all resistor color bands.

    """
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
