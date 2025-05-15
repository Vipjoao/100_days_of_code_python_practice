# Turtle challenge 3 is to draw different shapes with different colors
from turtle import Turtle, Screen
import colors
import random

tim = Turtle()
screen = Screen()

number_list = [3, 4, 5, 6, 7, 8, 9, 10]
def draw_shapes():
    """Draws shapes multiple shapes based on a list of numbers.
    The numbers represent how much sides each shape will have."""
    for n in number_list:
        tim.pencolor(random.choice(colors.tur_colors))
        for _ in range(n):
            tim.forward(100)
            tim.left(360/n)

draw_shapes()
screen.exitonclick()