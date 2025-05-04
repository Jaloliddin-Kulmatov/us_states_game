import turtle
import pandas

screen = turtle.Screen()
map_turtle = turtle.Turtle()
screen.setup(725,491)

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
map_turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()



guessed_list = []
while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct", prompt="What's the state name?").title()

    if answer_state == "Exit":
         new_data = pandas.DataFrame(states)
         new_data.to_csv("states_to_learn.csv")

         break

    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))
        guessed_list.append(answer_state)
        states.remove(answer_state)
