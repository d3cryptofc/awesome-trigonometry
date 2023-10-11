from contextlib import contextmanager
from typing import Union, List, Tuple, Optional

from turtle import Turtle


def get_turtle():
    """
    Get a customized turtle instance.
    """
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color('#333')
    turtle.pensize(1)
    return turtle


@contextmanager
def use_position(turtle: Turtle,
                 position: Tuple[Union[int, float], Union[int, float]],
                 penup: Optional[bool] = True):
    """
    A context manager to set the pen position and return to the
    previous position.

    Parameters:
        turtle:
            The turtle instance.

        position:
            Tuple containing X and Y positions.

        penup (default: True):
            Whether the pen should lift before setting the position.
    """
    # Getting pendown status.
    previous_pendown_status = turtle.pen()['pendown']

    # Getting current position to back posteriorly.
    previous_position = turtle.position()

    # Case `penup` parameter is True.
    if penup:
        turtle.penup()

    # Setting the position from `position` parameter.
    turtle.setposition(position)

    yield

    # Setting the position from `previous_position` parameter.
    turtle.setposition(previous_position)

    # Returning to previous pendown status.
    if previous_pendown_status:
        turtle.pendown()