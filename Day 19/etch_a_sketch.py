import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

def clear_screen():
    tim.home()
    tim.clear()

def etch_a_sketch():
    screen.listen()
    t.onkey(move_forward, 'Up')
    t.onkey(move_backward, 'Down')
    t.onkey(rotate_left, 'Left')
    t.onkey(rotate_right, 'Right')
    t.onkey(clear_screen, 'c')


etch_a_sketch()
screen.exitonclick()