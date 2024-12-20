"""Function to validate an ISBN-10 code."""


def is_valid(isbn: str) -> bool:
    """Validate an ISBN-10 code.

    Args:
        isbn (str): The ISBN-10 code, potentially with dashes.

    Returns:
        bool: True if the ISBN-10 is valid, otherwise False.

    """
    cleaned_isbn: str = isbn.replace("-", "")
    if len(cleaned_isbn) != 10:
        return False
    if not all(ch.isdigit() for ch in cleaned_isbn[:9]):
        return False
    if cleaned_isbn[-1] not in "0123456789X":
        return False
    check_sum: int = 0
    for index, character in enumerate(cleaned_isbn):
        value: int = 10 if character == "X" else int(character)
        weight: int = 10 - index
        check_sum += value * weight
    return check_sum % 11 == 0
