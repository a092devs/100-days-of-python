import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Indian States Game")
image = "./India-state.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title="State", prompt="What's another state's name ?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.xcor), int(state_data.ycor))
        t.write(answer_state)

screen.exitonclick()