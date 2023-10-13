"""
Teorema de pitágoras ilustrado.

1. Desenha cruz dos eixos.
2. Desenha um triângulo retângulo de tamanho aleatório.
3. Desenha o quadrado de todos os lados do triângulo.

---------------------------------------------------------

Pythagorean theorem illustrated.

1. Draw axes cross.
2. Draw a right-angled triangle of random size.
3. Draw the square of all sides of the triangle.
"""

import math
import random
import time
from turtle import Turtle, bgcolor
from typing import Union

import trigo


def draw_pythagoras(turtle: Turtle,
                    opposit: int,
                    adjacent: int,
                    scale: Union[int, float] = 10):
    # PT: Calculando a hipotenusa usando o teroma de pitágoras.
    # EN: Calculating the hypotenuse using the Pythagorean Theorem.
    # a² = b² + c²
    hypotenuse = math.sqrt(opposit ** 2 + adjacent ** 2)
 
    # PT: Aplicando uma proporção nos lados do triângulo.
    # EN: Scaling triangle sides.
    scaled_opposit = opposit / 2 * scale
    scaled_adjacent = adjacent / 2 * scale
    scaled_hypotenuse = hypotenuse * scale

    # PT: Criando gerador que desenha os 3 lados do triângulo.
    # EN: Creating generator to draw the 3 sides of the triangle.
    triangle_sides = trigo.draw.segment_chain(turtle, [
        # PT: Segmentos do cateto oposto.
        # EN: Opposit leg segments.
        (-scaled_adjacent, scaled_opposit),
        (-scaled_adjacent, -scaled_opposit),

        # PT: Segmento do cateto adjacente.
        # EN: Adjacent leg segment.
        (scaled_adjacent, -scaled_opposit),

        # PT: Segmento da hipotenusa.
        # EN: Hypotenuse segment.
        (-scaled_adjacent, scaled_opposit)
    ])

    # PT: Iniciando desenho do cateto oposto.
    # EN: Starting drawing the opposite leg.
    next(triangle_sides)
    next(triangle_sides)
    # PT: Escrevendo na tela a altura do cateto oposto.
    # EN: Writing on screen the opposit leg height.
    with trigo.tools.use_position(turtle, (-scaled_adjacent - 8, 0)):
        turtle.write(f'a = {opposit}', align='right')

    # PT: Iniciando desenho do cateto adjacente.
    # EN: Starting drawing the adjacent leg.
    next(triangle_sides)
    # PT: Escrevendo na tela a altura do cateto adjacente.
    # EN: Writing on screen the adjacent leg width.
    with trigo.tools.use_position(turtle, (0, -scaled_opposit - 22)):
        turtle.write(f'b = {adjacent}', align='center')
    
    # PT: Iniciando desenho da hipotenusa.
    # EN: Starting drawing the hypotenuse.
    next(triangle_sides)
    with trigo.tools.use_position(turtle, (20, 0)):
        turtle.write(f'c = {hypotenuse}', align='left')

    # PT: Pausa a execução da função para a próxima vez.
    # EN: Pause the execution of function for the next time.
    yield

    # PT: Definindo cor e tamanho da caneta para os próximos desenhos.
    # EN: Setting pen color and size for next drawings.
    turtle.color('#555')
    turtle.pensize(1)

    # PT: Desenhando quadrado do cateto oposto.
    # EN: Drawing square of the opposit leg.
    list(trigo.draw.segment_chain(turtle, [
        # PT: Segmento da aresta direita.
        # EN: Right edge segment.
        (-scaled_adjacent, scaled_opposit),
        (-scaled_adjacent - scaled_opposit * 2, scaled_opposit),

        # PT: Segmento da aresta superior.
        # EN: Top edge segment.
        (-scaled_adjacent - scaled_opposit * 2, -scaled_opposit),

        # PT: Segmento da aresta esquerda.
        # EN: Left edge segment.
        (-scaled_adjacent, -scaled_opposit)
    ]))

    # PT: Desenhando quadrado do cateto adjacente.
    # EN: Drwaing square of the adjacent leg.
    list(trigo.draw.segment_chain(turtle, [
        # PT: Segmento da aresta direita.
        # EN: Right edge segment.
        (-scaled_adjacent, -scaled_opposit),
        (-scaled_adjacent, -scaled_opposit - scaled_adjacent * 2),

        # PT: Segmento da aresta superior.
        # EN: Top edge segment.
        (scaled_adjacent, -scaled_opposit - scaled_adjacent * 2),

        # PT: Segmento da aresta esquerda.
        # EN: Left edge segment.
        (scaled_adjacent, -scaled_opposit)
    ]))


    # PT: Obtendo ângulo em que o quadrado da hipotenusa deve rotacionar.
    # EN: Obtaining angle by which the square of the hypotenuse should rotate.
    angle_y = scaled_adjacent / scaled_hypotenuse
    angle_x = scaled_opposit / scaled_hypotenuse
    # PT: Desenhando quadrado da hipotenusa.
    # EN: Drawing square of the hypotenuse. 
    list(trigo.draw.segment_chain(turtle, [
        # PT: Segmento da aresta direita.
        # EN: Right edge segment.
        (scaled_adjacent, -scaled_opposit),
        (scaled_adjacent + angle_x * scaled_hypotenuse * 2, -scaled_opposit + angle_y * scaled_hypotenuse * 2),

        # PT: Segmento da aresta superior.
        # EN: Top edge segment.
        (angle_x * scaled_hypotenuse * 2 - scaled_adjacent, angle_y * scaled_hypotenuse * 2 + scaled_opposit),

        # PT: Segmento da aresta esquerda.
        # EN: Left edge segment.
        (-scaled_adjacent, scaled_opposit)
    ]))

    yield


def main():
    # PT: Definindo a escala que aumentará o triângulo proporcionalmente.
    # EN: Defining the scale that will increase the triangle proportionally.
    SCALE = 20

    # PT: Definindo o tamanho dos catetos.
    # EN: Defining the size of the legs.
    OPPOSIT = random.randint(5, 10)
    ADJACENT = random.randint(5, 10)

    # PT: Definindo cor de fundo da janela.
    # EN: Setting canvas background color.
    bgcolor('black')

    # PT: Desenhando uma cruz no centro da tela.
    # EN: Drawing a cross in the center of the canvas.
    crossturtle = trigo.tools.get_turtle()
    crossturtle.pensize(1)
    trigo.draw.cross(
        distance=SCALE * (max(OPPOSIT, ADJACENT) / 2) + 40,
        turtle=crossturtle
    )

    # PT: Desenhando a ilustração do teorema de pitágoras.
    # EN: Drawing an illustration of the Pythagorean theorem.
    triangleturtle = trigo.tools.get_turtle()
    triangleturtle.color('#AAA')
    triangleturtle.pensize(3)
    pythagoras = draw_pythagoras(triangleturtle, OPPOSIT, ADJACENT, SCALE)
    # PT: Iniciando desenho do triângulo retângulo.
    # EN: Starting drawing of the right triangle.
    next(pythagoras)

    # PT: Desenhando um ponto no centro da tela.
    # EN: Drawing a dot in the center of the screen.
    centerturtle = trigo.tools.get_turtle()
    centerturtle.penup()
    centerturtle.setposition(0, 0)
    centerturtle.color('cyan')
    centerturtle.dot()

    # PT: Aguardando um intervalo de tempo.
    # EN: Waiting for a timeout.
    time.sleep(1)

    # PT: Apagando a cruz que foi desenhada.
    # EN: Erasing the cross that was drawn.
    crossturtle.clear()

    # PT: Iniciando desenho dos quadrados dos catetos.
    # EN: Starting to draw the squares of the legs.
    next(pythagoras)

    # PT: Aguardando um intervalo de tempo.
    # EN: Waiting for a timeout.
    time.sleep(2)

    # PT: Apagando tudo que foi desenhado.
    # EN: Erasing everything that was drawn.
    centerturtle.clear()
    triangleturtle.clear()


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('Exited.')
            exit(1)