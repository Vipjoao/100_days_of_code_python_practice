# Turtle challenge 2 is to draw a dashed line
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for _ in range(10): # Make a dashed line
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# for _ in range(4): # Bonus! How to make a dashed square
#     tim.left(90)
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()