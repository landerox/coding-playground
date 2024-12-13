"""Function for determining Bob's response based on input."""


def response(hey_bob: str) -> str:
    """Determine Bob's response based on the input.

    Args:
        hey_bob (str): The input statement or question directed at Bob.

    Returns:
        str: Bob's response.

    """
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if hey_bob.endswith("?"):
        return "Sure."
    return "Whatever."
