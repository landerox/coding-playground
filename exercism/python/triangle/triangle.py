"""Functions to classify triangles based on the lengths of their sides."""

from typing import List


def is_valid_triangle(sides: List[float]) -> bool:
    """Check if three sides form a valid triangle.

    A valid triangle must have all sides greater than zero, and the sum of
    any two sides must be greater than or equal to the third side.

    Args:
        sides (List[float]): The lengths of the three sides.

    Returns:
        bool: True if the sides form a valid triangle, False otherwise.

    """
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c


def equilateral(sides: List[float]) -> bool:
    """Determine if a triangle is equilateral.

    An equilateral triangle has all three sides of equal length.

    Args:
        sides (List[float]): The lengths of the three sides.

    Returns:
        bool: True if the triangle is equilateral, False otherwise.

    """
    return is_valid_triangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides: List[float]) -> bool:
    """Determine if a triangle is isosceles.

    An isosceles triangle has at least two sides of equal length.

    Args:
        sides (List[float]): The lengths of the three sides.

    Returns:
        bool: True if the triangle is isosceles, False otherwise.

    """
    return is_valid_triangle(sides) and (
        sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    )


def scalene(sides: List[float]) -> bool:
    """Determine if a triangle is scalene.

    A scalene triangle has all sides of different lengths.

    Args:
        sides (List[float]): The lengths of the three sides.

    Returns:
        bool: True if the triangle is scalene, False otherwise.

    """
    return is_valid_triangle(sides) and sides[0] != sides[1] != sides[2] != sides[0]
