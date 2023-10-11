"""
Desenhando um círculo e preenchendo com segmentos coloridos.

1. Desenha cruz dos eixos.
2. Desenha a circunferencia do círculo.
3. Desenha segmentos coloridos no interior do circulo, resultando em um preenchimento colorido.

---------------------------------------------------------

Drawing a circle and filling it with colorful segments.

1. Draw the cross of the axes.
2. Draw the circumference of the circle.
3. Draw colored segments inside the circle, resulting in a colored fill.
"""

import colorsys
import math
import random
import time
import turtle

import trigo


def main():
    # Setting the screen background.
    turtle.bgcolor('black')
    # Setting the color mode to RGB.
    turtle.colormode(255)

    # Setting a random circle radius.
    radius = random.randint(50, 150)

    # Getting a turtle instance to draw the cross.
    crossturtle = trigo.tools.get_turtle()
    # Setting the pen size.
    crossturtle.pensize(4)
    # Drawing the cross.
    trigo.draw.cross(crossturtle, radius, show_dots=False)

    # Getting a turtle instance to draw the circle circunference.
    circleturtle = trigo.tools.get_turtle()
    # Setting the pen size.
    circleturtle.pensize(4)
    # Drawing the circle circunference.
    trigo.draw.circle(circleturtle, radius)

    # Getting a turtle instance to draw the fill of the circle.
    fillturtle = trigo.tools.get_turtle()
    # Setting animation velocity to ultra fast.
    fillturtle.speed(0)
    # Setting the pen size.
    fillturtle.pensize(3)
    # Sequence iteration from 0 to 360.
    for angle in range(0, 360 + 1):
        # Transforming the angle from 0 to 360 into a number between 0 and 1
        # converting from HSL (Hue, Saturation, Lightness) color system
        # to RGB (Red, Green, Blue) color system.
        color = colorsys.hls_to_rgb(h=angle / 360, l=0.5, s=1)

        # Converting numbers from between 0 and 1 to between 0 and 255.
        color = list(map(lambda x: int(x * 255), color))

        # Setting the pen color.
        fillturtle.color(color)

        # Drawing colorful segment.
        trigo.draw.segment(
            turtle=fillturtle,
            start=(0, 0),
            end=(
                math.cos(math.radians(angle)) * radius,
                math.sin(math.radians(angle)) * radius
            ),
            show_dots=False
        )

    # Waiting for 1 second.
    time.sleep(1)

    # Erasing all drawing parts.
    crossturtle.clear()
    circleturtle.clear()
    fillturtle.clear()


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('Exited.')
            exit(1)