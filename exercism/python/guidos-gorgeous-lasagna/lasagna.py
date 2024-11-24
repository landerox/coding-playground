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
    """Calculate the remaining bake time.

    :param elapsed_bake_time: int - minutes already spent baking.
    :return: int - remaining bake time in minutes.

    This function subtracts the elapsed baking time from the
    EXPECTED_BAKE_TIME constant to calculate the time left.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """Calculate preparation time for a given number of layers.

    :param layers: int - number of lasagna layers.
    :return: int - total preparation time in minutes.

    Multiplies the number of layers by the PREPARATION_TIME constant
    to calculate the total preparation time.
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """Calculate total elapsed time for preparing and baking.

    :param layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed in minutes.
    :return: int - total elapsed cooking time in minutes.

    Adds the preparation time (based on the number of layers) to the
    elapsed baking time to compute the total cooking time.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
