"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    prefixed_word = f"un{word}"
    return prefixed_word


def make_word_groups(vocab_words: list) -> str:
    """Create a string with a prefix and words prefixed, separated by ' :: '.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    words_with_applied_prefix = [f"{prefix}{word}" for word in vocab_words[1:]]
    result_string = f"{prefix} :: " + " :: ".join(words_with_applied_prefix)
    return result_string


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    root_word = word[:-4]
    adjusted_word = root_word[:-1] + "y" if root_word.endswith("i") else root_word
    return adjusted_word


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    words_in_sentence = sentence.strip(".").split()
    adjective_word = words_in_sentence[index]
    verb_form = f"{adjective_word}en"
    return verb_form
