"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list, number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds


def card_average(hand: list) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list) -> bool:
    """Return if (avg of first and last values) OR ('middle' card)==calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    true_average = card_average(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    return true_average in {first_last_avg, middle_card}


def average_even_is_average_odd(hand: list) -> bool:
    """Return if (average of even indexed values) == (average of odd indexed values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_cards = [hand[index] for index in range(0, len(hand), 2)]
    odd_cards = [hand[index] for index in range(1, len(hand), 2)]
    return card_average(even_cards) == card_average(odd_cards)


def maybe_double_last(hand: list) -> list:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand and hand[-1] == 11:
        hand[-1] *= 2
    return hand
