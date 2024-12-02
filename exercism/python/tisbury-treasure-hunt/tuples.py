"""Functions to help Azara and Rui locate pirate treasure."""

from typing import Tuple, Union


def get_coordinate(record: Tuple[str, str]) -> str:
    """Extract coordinate from treasure record.

    :param record: tuple - A tuple with two elements: (treasure, coordinate).
    :return: str - The extracted map coordinate from the tuple.
    """
    _, coordinate = record
    return coordinate


def convert_coordinate(coordinate: str) -> Tuple[str, str]:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate.
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(
    azara_record: Tuple[str, str], rui_record: Tuple[str, Tuple[str, str], str]
) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2),
    quadrant) trio.
    :return: bool - Do the coordinates match?
    """
    azara_coordinate = convert_coordinate(azara_record[1])
    rui_coordinate = rui_record[1]
    return azara_coordinate == rui_coordinate


def create_record(
    azara_record: Tuple[str, str], rui_record: Tuple[str, Tuple[str, str], str]
) -> Union[Tuple[str, str, str, Tuple[str, str], str], str]:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - The combined record (if compatible), or "not a match".
    """
    if compare_records(azara_record, rui_record):
        treasure_name = azara_record[0]
        azara_coordinate = azara_record[1]
        location_name = rui_record[0]
        rui_coordinate = rui_record[1]
        quadrant = rui_record[2]
        return treasure_name, azara_coordinate, location_name, rui_coordinate, quadrant
    return "not a match"


def clean_up(
    combined_record_group: Tuple[Tuple[str, str, str, Tuple[str, str], str], ...],
) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - All combined records from both participants.
    :return: str - Cleaned, multi-line string representation of the records.
    """
    cleaned_records = []
    for record in combined_record_group:
        treasure_name, _, location_name, coordinate_tuple, quadrant = record
        cleaned_records.append(
            f"('{treasure_name}', '{location_name}', {coordinate_tuple}, '{quadrant}')"
        )
    return "\n".join(cleaned_records) + "\n"
