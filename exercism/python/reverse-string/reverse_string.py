"""Function to reverse a given string."""


def reverse(text: str) -> str:
    """Reverse the input string.

    Args:
        text (str): The string to be reversed.

    Returns:
        str: The reversed version of the input string.

    """
    reversed_text: str = text[::-1]
    return reversed_text
