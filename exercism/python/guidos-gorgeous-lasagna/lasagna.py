"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Global constants
EXPECTED_BAKE_TIME = 40  # Expected baking time (in minutes)
PREPARATION_TIME = 2  # Time required to prepare each layer (in minutes)


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the remaining bake time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """Calculate preparation time based on the number of layers."""
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total elapsed cooking time."""
    return preparation_time_in_minutes(layers) + elapsed_bake_time
