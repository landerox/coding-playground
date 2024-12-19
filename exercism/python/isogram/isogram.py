"""Function to determine if a word or phrase is an isogram."""


def is_isogram(string: str) -> bool:
    """Determine if a word or phrase is an isogram.

    An isogram is a word or phrase without repeating letters,
    allowing spaces and hyphens to appear multiple times.

    Args:
        string (str): The word or phrase to evaluate.

    Returns:
        bool: True if the input is an isogram, False otherwise.

    """
    normalized_string: str = "".join(char for char in string.lower() if char.isalpha())

    seen_letters: set[str] = set()

    for char in normalized_string:
        if char in seen_letters:
            return False
        seen_letters.add(char)

    return True
