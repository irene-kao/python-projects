# This is a digital etch-a-sketch

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter():
    tim.left(5)

def move_clockwise():
    tim.right(5)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Displays instructions
tim.penup()
tim.hideturtle()
tim.goto(-250,220)
tim.write("Welcome to Etch-a-sketch!",font=("Arial",15,"normal"))
tim.goto(-250,200)
tim.write("Use the left and right arrow keys to change the direction of your pen.")
tim.goto(-250,190)
tim.write("Use the up and down arrows to draw.")
tim.goto(-250,180)
tim.write("Press the space bar to start.")
tim.goto(0,0)
tim.showturtle()

screen.listen()
screen.onkey(fun=move_forward, key="Up")
screen.onkey(fun=move_backward, key="Down")
screen.onkey(fun=move_counter, key="Left")
screen.onkey(fun=move_clockwise, key="Right")
screen.onkey(fun=clear, key="space")

screen.exitonclick()
