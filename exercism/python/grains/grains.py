"""Functions which help calculate grains of wheat on a chessboard."""


def square(square_number: int) -> int:
    """Calculate the number of grains on a given square.

    Args:
        square_number (int): The square number (1 to 64).

    Returns:
        int: The number of grains on the given square.

    Raises:
        ValueError: If the square number is not between 1 and 64.

    """
    if square_number < 1 or square_number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (square_number - 1)


def total() -> int:
    """Calculate the total number of grains on the chessboard.

    Returns:
        int: The total number of grains on the chessboard.

    """
    return sum(square(square_number) for square_number in range(1, 65))
