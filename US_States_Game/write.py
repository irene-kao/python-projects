from turtle import Turtle

class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.write_me()
        self.xcor = answer_x

    def write_me(self):
        text = Turtle()
        text.hideturtle()
        text.penup()
        text.goto(answer_x, answer_y)
        text.write(answer_format)