"""Functions to keep track and alter inventory."""

from typing import Dict, List, Tuple


def create_inventory(items: List[str]) -> Dict[str, int]:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {item: items.count(item) for item in set(items)}
    return inventory


def add_items(inventory: Dict[str, int], items_to_add: List[str]) -> Dict[str, int]:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items_to_add:
        current_count = inventory.get(item, 0)
        inventory[item] = current_count + 1
    return inventory


def decrement_items(
    inventory: Dict[str, int], items_to_decrement: List[str]
) -> Dict[str, int]:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items_to_decrement:
        if item in inventory:
            updated_count = max(inventory[item] - 1, 0)
            inventory[item] = updated_count
    return inventory


def remove_item(inventory: Dict[str, int], item_to_remove: str) -> Dict[str, int]:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed.
                    Current inventory if item does not match.
    """
    inventory.pop(item_to_remove, None)
    return inventory


def list_inventory(inventory: Dict[str, int]) -> List[Tuple[str, int]]:
    """List Available Inventory.

    Create a list containing only available (item_name, item_count > 0)
    pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    available_items = [
        (item_name, item_count)
        for item_name, item_count in inventory.items()
        if item_count > 0
    ]
    return available_items
