import random
from turtle import Turtle,Screen
from random import randint
import colorgram
tim= Turtle()
screen =Screen()
screen.colormode(255)

colors= colorgram.extract('damien-hirst.jpg',10)
rgb_colors=[]
for color in  colors:
    r=color.rgb.r
    g=color.rgb.b
    b=color.rgb.g
    rgb_tupple=(r,g,b)
    rgb_colors.append(rgb_tupple)
for col in range(11):
    for row in range(11):
        color= random.choice(rgb_colors)
        tim.dot(30,color)
        tim.penup()
        tim.forward(50)



screen.exitonclick()
