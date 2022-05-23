# This program starts a race of 6 turtles and allows the user to guess which turtle will win.

from turtle import Turtle, Screen
import random

def print_hello():
    """Prints hello"""
    print("hello")

help(round)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet ", prompt="Which turtle will win the race? Enter the color: (red/orange/yellow/green/blue/purple)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_house = []

finish_line = Turtle()
finish_line.penup()
finish_line.setposition(x=200,y=180)
finish_line.pendown()
finish_line.goto(x=200,y=-180)
finish_line.hideturtle()

y_pos = 130
for turtle_hatchery in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_hatchery])
    turtle.penup()
    turtle.setposition(x=-200, y=y_pos)
    y_pos -= 50
    turtle_house.append(turtle)

if user_bet:
    race_on = True

winner = ""
while race_on:
    for turtle in turtle_house:
        if turtle.xcor() >= 180:
            winner = turtle
            print(winner.color())
            race_on = False
        turtle.forward(random.randint(0, 10))

winning_color = winner.fillcolor()
if user_bet == winning_color:
    print(f"Congrats! You win.")
else:
    print(f"Sorry, you lost. The winner was {winning_color}.")
screen.exitonclick()
