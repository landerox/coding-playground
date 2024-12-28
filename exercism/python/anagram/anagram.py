"""Function to find anagrams of a given target word from a set of candidate words."""

from typing import List


def find_anagrams(target_word: str, candidate_words: List[str]) -> List[str]:
    """Find the subset of candidate words that are anagrams of the target word.

    An anagram is a rearrangement of letters to form a new word. Words are
    considered case-insensitive but should retain their original casing
    in the result.

    Args:
        target_word (str): The target word to compare against.
        candidate_words (List[str]): A list of candidate words to check.

    Returns:
        List[str]: A list of words from the candidates that are anagrams
                   of the target word.

    """
    normalized_target = sorted(target_word.lower())
    anagrams = [
        candidate
        for candidate in candidate_words
        if candidate.lower() != target_word.lower()
        and sorted(candidate.lower()) == normalized_target
    ]
    return anagrams
