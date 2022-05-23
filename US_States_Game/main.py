# Do you know all 51 U.S. States? Try out this game to test your knowledge.

from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)  # shape can be any image file
turtle.shape(image)  # after add image to screen, can be used by turtle
screen.tracer(0)

states_data = pandas.read_csv("50_states.csv")

game_is_on = True
score = 0
correct = []
while game_is_on:
    answer = screen.textinput(title=f"{score}/50", prompt="Type in a state's name")
    answer_format = answer.title()
    all_states = states_data["state"].to_list()
    if score == 50:
        game_is_on = False
        print("You win!")
    elif answer_format == "Exit":
        game_is_on = False
        print(f"You got the following states correct: {correct}")
        need_learn = [state for state in all_states if state not in correct]
        break
    elif answer_format in all_states:
        correct.append(answer_format)
        answer_row = states_data[states_data["state"] == answer_format]
        score += 1

        text = Turtle()
        text.hideturtle()
        text.penup()
        text.goto(int(answer_row["x"]), int(answer_row["y"]))
        text.write(answer_row.state.item())
        screen.update()

need_learn_pd = pandas.DataFrame(need_learn)
need_learn.to_csv("learn_this.csv")

# Code for getting x & y coordinates
# define a function click(x, y): print(x, y)
# turtle.onscreenclick(click) - listens for click
# turtle.mainloop() -- Keeps screen open even when code done running