from turtle import Turtle
from typing import Union, Tuple, Optional


def segment(turtle: Turtle,
            start: Tuple[Union[int, float], Union[int, float]],
            end: Tuple[Union[int, float], Union[int, float]],
            show_dots: Optional[bool] = True):
    """
    Draw a segment between two points.

    Parameters:
        turtle:
            The turtle instance.

        start:
            Tuple containing X and Y start positions.

        end:
            Tuple containing X and Y end positions.

        show_dots (default: True):
            Whether dots should be drawn at the two points.
    """
    # Setting point of start.
    turtle.penup()
    turtle.setposition(start)
    if show_dots:
        turtle.dot()

    # Setting point of end.
    turtle.pendown()
    turtle.setposition(end)
    if show_dots:
        turtle.dot()