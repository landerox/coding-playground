"""Function to translate resistor color bands into a readable ohm value."""

from typing import Dict, List

COLOR_CODES: Dict[str, int] = {
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

TOLERANCES: Dict[str, str] = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}


def resistor_label(colors: List[str]) -> str:
    """Translate resistor color bands into a readable ohm value with tolerance.

    Args:
        colors (List[str]): A list of color bands representing a resistor.

    Returns:
        str: A human-readable string of the resistor's value with tolerance.

    """
    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        base_value = int("".join(str(COLOR_CODES[color]) for color in colors[:2]))
        multiplier = 10 ** COLOR_CODES[colors[2]]
        tolerance = TOLERANCES[colors[3]]
    elif len(colors) == 5:
        base_value = int("".join(str(COLOR_CODES[color]) for color in colors[:3]))
        multiplier = 10 ** COLOR_CODES[colors[3]]
        tolerance = TOLERANCES[colors[4]]
    else:
        raise ValueError("Invalid number of color bands. Must be 1, 4, or 5.")

    resistance = base_value * multiplier

    if resistance >= 1_000_000:
        resistance_str = (
            f"{resistance / 1_000_000:.2f}".rstrip("0").rstrip(".") + " megaohms"
        )
    elif resistance >= 1_000:
        resistance_str = (
            f"{resistance / 1_000:.2f}".rstrip("0").rstrip(".") + " kiloohms"
        )
    else:
        resistance_str = f"{resistance} ohms"

    return f"{resistance_str} {tolerance}"
