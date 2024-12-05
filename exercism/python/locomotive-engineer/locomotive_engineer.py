"""Functions which helps the locomotive engineer to keep track of the train."""

from typing import Dict, List, Tuple


def get_list_of_wagons(*wagon_ids: int) -> List[int]:
    """Return a list of wagons.

    :param wagon_ids: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagon_ids)


def fix_list_of_wagons(wagon_ids: List[int], missing_wagon_ids: List[int]) -> List[int]:
    """Fix the list of wagons.

    :param wagon_ids: list - the list of wagons.
    :param missing_wagon_ids: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    locomotive = wagon_ids.pop(2)
    reordered_wagons = wagon_ids[2:] + wagon_ids[:2]
    return [locomotive] + missing_wagon_ids + reordered_wagons


def add_missing_stops(route: Dict[str, str], **stops: str) -> Dict[str, List[str]]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param stops: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = list(stops.values())
    return route


def extend_route_information(
    route: Dict[str, str], additional_route_info: Dict[str, str]
) -> Dict[str, str]:
    """Extend route information with additional_route_info.

    :param route: dict - the route information.
    :param additional_route_info: dict - extra route information.
    :return: dict - extended route information.
    """
    route.update(additional_route_info)
    return route


def fix_wagon_depot(
    wagon_rows: List[List[Tuple[int, str]]],
) -> List[List[Tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagon_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(row) for row in zip(*wagon_rows)]
