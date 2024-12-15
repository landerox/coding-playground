"""Functions to calculate the score of a dart game."""


def score(dart_x: float, dart_y: float) -> int:
    """Calculate the score for a dart based on its coordinates.

    Args:
        dart_x (float): The x-coordinate of the dart's position.
        dart_y (float): The y-coordinate of the dart's position.

    Returns:
        int: The score based on where the dart lands.

    """
    dart_squared_distance: float = dart_x**2 + dart_y**2
    if dart_squared_distance <= 1**2:
        return 10
    elif dart_squared_distance <= 5**2:
        return 5
    elif dart_squared_distance <= 10**2:
        return 1
    return 0
