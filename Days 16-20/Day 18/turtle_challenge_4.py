# Turtle challenge 4 is to draw a random path with different colors, pen thickness and turtle speed
import turtle as t
import colors
import random

tim = t.Turtle()
screen = t.Screen()

angles = (0, 90, 180, 270) # Tuples are different from lists, tuples can't be changed
def random_path_drawing():
    tim.pensize(7)
    for _ in range(500):
        tim.speed(100)
        tim.setheading(random.choice(angles))
        tim.pencolor(colors.random_color())
        tim.forward(10)


random_path_drawing()
screen.exitonclick()