"""Function to determine if a given sentence is a pangram."""

from string import ascii_lowercase


def is_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram.

    This function verifies if the input sentence contains every letter of the
    English alphabet at least once, regardless of case.

    Args:
        sentence (str): The sentence to evaluate.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.

    """
    normalized_sentence: set[str] = set(sentence.lower())
    alphabet_set: set[str] = set(ascii_lowercase)
    return alphabet_set.issubset(normalized_sentence)
