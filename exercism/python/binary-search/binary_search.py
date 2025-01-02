"""Function to implement a binary search algorithm."""

from typing import List


def find(search_list: List[int], value: int) -> int:
    """Perform a binary search on a sorted list to find the index of a value.

    This function assumes the input list is sorted in ascending order. If the
    value is not found in the list, a ValueError is raised.

    Args:
        search_list (List[int]): The sorted list of integers to search.
        value (int): The integer value to find.

    Returns:
        int: The index of the value in the list.

    Raises:
        ValueError: If the value is not found in the list.

    """
    left: int = 0
    right: int = len(search_list) - 1

    while left <= right:
        middle: int = (left + right) // 2
        middle_value: int = search_list[middle]

        if middle_value == value:
            return middle
        elif middle_value < value:
            left = middle + 1
        else:
            right = middle - 1

    raise ValueError("value not in array")
