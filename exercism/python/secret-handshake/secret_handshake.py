"""Function to convert a binary string to a sequence of secret handshake actions."""

from typing import List


def commands(binary_str: str) -> List[str]:
    """Convert a binary string to a sequence of secret handshake actions.

    The function interprets the binary string as a series of actions, where
    each bit corresponds to a specific action in the handshake protocol.
    The reverse bit modifies the sequence order if set.

    Args:
    ----
        binary_str (str): A string representing a binary number.

    Returns:
    -------
        list[str]: A list of actions in the order they should be performed.

    """
    action_map = ["wink", "double blink", "close your eyes", "jump"]
    actions = []
    binary_length = len(binary_str)

    for i in range(min(4, binary_length)):
        if binary_str[-(i + 1)] == "1":
            actions.append(action_map[i])

    if binary_length > 4 and binary_str[-5] == "1":
        actions.reverse()

    return actions
