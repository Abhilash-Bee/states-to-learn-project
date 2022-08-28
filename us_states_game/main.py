import time
import turtle
import pandas

screen = turtle.Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
screen.setup(730, 480)
screen.title("US STATES GAME")
mothi = turtle.Turtle()
mothi.penup()
mothi.hideturtle()

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(f"{len(guessed_states)}/50 states", "Enter the state in US:: ").title()
    if user_input == "Exit":
        break
    if user_input in all_states:
        position = data[data["state"] == user_input]
        mothi.goto(int(position["x"]), int(position["y"]))
        mothi.write(arg=user_input, align="center", font=("courier", 10, "normal"))
        guessed_states.append(user_input)
        time.sleep(1)


remaining_state = [state for state in all_states if state not in guessed_states]

data_to_study = pandas.DataFrame(remaining_state)
data_to_study.to_csv("states_to_learn.txt")
