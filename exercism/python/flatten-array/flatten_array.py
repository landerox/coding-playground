"""Function to flatten a nested list and remove nil/null values."""

from typing import List, Union

NestedList = Union[int, float, str, None, List["NestedList"]]


def flatten(iterable: List[NestedList]) -> List[Union[int, float, str]]:
    """Flatten a nested list and remove nil/null values.

    This function recursively traverses the input nested list and collects
    all non-nil/null values into a single flattened list.

    Args:
        iterable (List[NestedList]): The input nested list.

    Returns:
        List[Union[int, float, str]]: A single flattened list with all
        non-nil/null values.

    """
    flattened_list: List[Union[int, float, str]] = []

    for item in iterable:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        elif item is not None:
            flattened_list.append(item)

    return flattened_list
