"""Functions to automate Conda airlines ticketing system."""

from typing import Dict, Generator, List


def generate_seat_letters(total_letters: int) -> Generator[str, None, None]:
    """Generate a series of seat letters for an airplane.

    Args:
        total_letters (int): The total number of seat letters to be generated.

    Returns:
        Generator[str, None, None]: A generator that yields seat letters.

    """
    seat_letters = ["A", "B", "C", "D"]
    for index in range(total_letters):
        yield seat_letters[index % len(seat_letters)]


def generate_seats(total_seats: int) -> Generator[str, None, None]:
    """Generate a series of seat identifiers for an airplane.

    Args:
        total_seats (int): The total number of seats to be generated.

    Returns:
        Generator[str, None, None]: A generator that yields seat identifiers.

    """
    seat_count = 0
    row_number = 1

    while seat_count < total_seats:
        if row_number == 13:
            row_number += 1
            continue
        for seat_letter in generate_seat_letters(4):
            yield f"{row_number}{seat_letter}"
            seat_count += 1
            if seat_count == total_seats:
                return
        row_number += 1


def assign_seats(passenger_names: List[str]) -> Dict[str, str]:
    """Assign seats to passengers.

    Args:
        passenger_names (list[str]): A list of passenger names.

    Returns:
        dict: A dictionary mapping passenger names to assigned seat numbers.

    """
    seat_generator = generate_seats(len(passenger_names))
    return {passenger_name: next(seat_generator) for passenger_name in passenger_names}


def generate_codes(
    seat_numbers: List[str], flight_id: str
) -> Generator[str, None, None]:
    """Generate unique ticket codes.

    Args:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): The flight identifier.

    Returns:
        Generator[str, None, None]: A generator that yields unique ticket codes.

    """
    for seat_number in seat_numbers:
        padded_code = f"{seat_number}{flight_id}".ljust(12, "0")
        yield padded_code
