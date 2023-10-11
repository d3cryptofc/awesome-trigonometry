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

