import math
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


def cross(turtle: Turtle,
          distance: Union[int, float],
          show_dots: Optional[bool] = True):
    """
    Draw a centered cross.

    Parameters:
        turtle:
            The turtle instance.

        distance:
            Distance from the center.

        show_dots (default: True):
            Whether dots should be drawn at the two points.
    """
    # Drawing X axis segment. 
    segment(
        turtle=turtle,
        start=(-distance, 0),
        end=(distance, 0),
        show_dots=show_dots
    )

    # Drawing Y axis segment.
    segment(
        turtle=turtle,
        start=(0, -distance),
        end=(0, distance),
        show_dots=show_dots
    )


def circle(turtle: Turtle, radius: Union[int, float]):
    """
    Draw a centered circle.

    Parameters:
        turtle:
            The turtle instance.

        radius:
            Circle radius, distance from the center.
    """
    # Putting the pen up.
    turtle.penup()

    # Setting the initial position of the pen at the beginning of the circle.
    turtle.setposition(radius, 0)

    # Putting the pen down.
    turtle.pendown()

    # Sequence iteration from 0 to 360 (one full turn, it draws the circunference).
    for angle in range(0, 360 + 1, 10):
        # Converting angle to radians.
        radians = math.radians(angle)

        # Obtaining cosine of the angle and multiplying by the radius.
        x = math.cos(radians) * radius

        # Obtaining sine of the angle and multiplying by the radius.
        y = math.sin(radians) * radius

        # Setting the pen position.
        turtle.setposition(x, y)