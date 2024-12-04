"""Functions to manage a users shopping cart items."""

from typing import Dict, Iterable, List, Union


def add_item(
    current_cart: Dict[str, int], items_to_add: Iterable[str]
) -> Dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes: Iterable[str]) -> Dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    for note in notes:
        cart[note] = cart.get(note, 0) + 1
    return cart


def update_recipes(
    ideas: Dict[str, str], recipe_updates: Dict[str, str]
) -> Dict[str, str]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart: Dict[str, int]) -> Dict[str, int]:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(
    cart: Dict[str, int], aisle_mapping: Dict[str, List[Union[str, bool]]]
) -> Dict[str, List[Union[int, str, bool]]]:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment = {}
    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            fulfillment[item] = [quantity, aisle, refrigeration]

    return dict(sorted(fulfillment.items(), key=lambda x: x[0], reverse=True))


def update_store_inventory(
    fulfillment_cart: Dict[str, List[Union[int, str, bool]]],
    store_inventory: Dict[str, List[Union[int, str, bool]]],
) -> Dict[str, List[Union[int, str, bool]]]:
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory.
    :return: dict - store_inventory updated.
    """
    for item, details in fulfillment_cart.items():
        if item in store_inventory:
            store_quantity = store_inventory[item][0]
            order_quantity = details[0]
            new_quantity = max(0, store_quantity - order_quantity)
            store_inventory[item][0] = new_quantity
            if new_quantity == 0:
                store_inventory[item][0] = "Out of Stock"
    return store_inventory
