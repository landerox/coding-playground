"""Functions to determine whether a given year is a leap year."""


def leap_year(year: int) -> bool:
    """Determine if a given year is a leap year in the Gregorian calendar.

    A leap year occurs:
    - Every year that is evenly divisible by 4.
    - Except for years evenly divisible by 100, which are not leap years unless they
      are also divisible by 400.

    Args:
        year (int): The year to evaluate.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
