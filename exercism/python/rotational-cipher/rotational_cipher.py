"""Function to implement a rotational cipher (Caesar cipher) for text encryption."""


def rotate(text: str, key: int) -> str:
    """Perform a rotational cipher on the given text with the specified key.

    Each alphabetic character is shifted by the value of the key, while preserving
    the case of the character and ignoring non-alphabetic characters.

    Args:
        text (str): The input text to be encrypted or decrypted.
        key (int): The rotational cipher key (0-26).

    Returns:
        str: The transformed text after applying the rotational cipher.

    """
    result: str = ""
    for char in text:
        if char.isalpha():
            base: int = ord("A") if char.isupper() else ord("a")
            shifted_char: str = chr((ord(char) - base + key) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result
