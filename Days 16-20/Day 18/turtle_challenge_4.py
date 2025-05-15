# Turtle challenge 4 is to draw a random path with different colors, pen thickness and turtle speed
from turtle import Turtle, Screen
import colors
import random

tim = Turtle()
screen = Screen()

angles = (0, 90, 180, 270)
def random_path_drawing():
    tim.pensize(7)
    for _ in range(500):
        tim.speed(100)
        tim.setheading(random.choice(angles))
        tim.pencolor(random.choice(colors.tur_colors))
        tim.forward(10)


random_path_drawing()
screen.exitonclick()