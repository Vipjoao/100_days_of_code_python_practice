# Turtle challenge 5 is to draw a spirograph
import turtle as t
import colors

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
t.speed("fastest")

def draw_spirograph():
    radius = 100  # Radius of each circle
    circles = 72  # Number of circles in the pattern (usually divisible by 360)
    angle = 360 / circles  # Angle between circles
    for _ in range(circles):
        t.pencolor(colors.random_color())
        t.circle(radius)
        t.left(angle)

draw_spirograph()
screen.exitonclick()