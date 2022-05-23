# This code generates a random Hirst Painting using color palette from image.jpeg

import colorgram
from turtle import Turtle, Screen
import random

color_list = [
    (25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56),
 (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90),
 (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86),
 (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190),
 (242, 205, 8), (89, 48, 31), (39, 46, 81), (26, 97, 94)
    ]

# colors = colorgram.extract("image.jpeg", 42)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)
tim.hideturtle()

x = -250
y = -250
for value in range(10):
    tim.penup()
    y += 50
    tim.setposition(x, y)
    for value2 in range(10):
        tim.pendown()
        my_color = random.choice(color_list)
        tim.dot(20, my_color)
        tim.penup()
        tim.forward(50)

screen.exitonclick()
