import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guess_states = []



while len(guess_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()


    #If ans_state is one of the states on in all the states of the 50_states_csv
        #If they got it right:
            #Create a turtle to write the name of the state at the state's x and y coordinate.
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


# states_to learn.csv