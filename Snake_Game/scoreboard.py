from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Comic Sans", 20, "normal")
FONT2 = ("Comic Sans", 50, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.setposition(0, 250)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT1)

    def count_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT1)

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT2)