import turtle

import pandas

screen= turtle.Screen()
screen.title('u.s.quiz game')
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_core(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_core)
data= pandas.read_csv('50_states.csv')
states=data['state'].to_list()
guessed_states=[]
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="whats another states name?").title()
    if answer_state =='Exit':
        missing_list=[state for state in states if state not in guessed_states]
        # missing_list=[]
        # for state in states:
        #     if state not in guessed_states:
        #         missing_list.append(state)
        df=pandas.DataFrame(missing_list)
        df.to_csv('missing_data.csv')
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        # t.write(state_data.state.item())
        t.write(answer_state)
print(guessed_states)


