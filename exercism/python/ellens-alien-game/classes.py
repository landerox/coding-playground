"""Solution to Ellen's Alien Game exercise."""

from typing import List, Tuple


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    total_aliens_created: int - Class variable to count total aliens created.
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Placeholder for collision detection logic.

    """

    total_aliens_created: int = 0

    def __init__(self, x_coordinate: int, y_coordinate: int, health: int = 3) -> None:
        """Initialize an Alien object with its coordinates and health.

        Args:
        ----
        x_coordinate : int
            The x-axis coordinate of the Alien.
        y_coordinate : int
            The y-axis coordinate of the Alien.
        health : int, optional
            The initial health of the Alien (default is 3).

        """
        self.x_coordinate: int = x_coordinate
        self.y_coordinate: int = y_coordinate
        self.health: int = health
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Decrease the Alien's health by one point.

        Ensures that the health does not go below zero.
        """
        self.health = max(0, self.health - 1)

    def is_alive(self) -> bool:
        """Check if the Alien is alive.

        Returns
        -------
        bool
            True if the Alien's health is greater than zero, False otherwise.

        """
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Move the Alien to new coordinates.

        Args:
        ----
        new_x_coordinate : int
            The new x-axis coordinate for the Alien.
        new_y_coordinate : int
            The new y-axis coordinate for the Alien.

        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other: "Alien") -> None:
        """Detect collisions with the given Alien.

        This method checks if this object collides with the provided Alien object.
        If a collision is detected, appropriate actions can be taken.

        Args:
        ----
        other : Alien
            The Alien object to check for collision.

        Returns:
        -------
        None

        """


def new_aliens_collection(coordinates_list: List[Tuple[int, int]]) -> List[Alien]:
    """Create a collection of Alien objects from a list of coordinates.

    Args:
    ----
    coordinates_list : List[Tuple[int, int]]
        A list of tuples where each tuple represents (x, y) coordinates.

    Returns:
    -------
    List[Alien]
        A list of Alien objects initialized with the given coordinates.

    """
    return [Alien(x_coord, y_coord) for x_coord, y_coord in coordinates_list]
