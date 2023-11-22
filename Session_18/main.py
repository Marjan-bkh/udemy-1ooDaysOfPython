import random
from turtle import Turtle,Screen
from random import randint
tim= Turtle()
screen =Screen()

# for _ in range(10):
#     tim.right(90)
#     tim.forward(200)

# screen.exitonclick()


# for i in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# screen.exitonclick()

# for i in range(3,11):
#     degree= 360/i
#     random_color = randint(1, 255), randint(1, 255), randint(1, 255)
#     screen.colormode(255)
#     tim.pencolor(random_color)
#     for l in range(i):
#         tim.right(degree)
#         tim.forward(100)
#
# screen.exitonclick()


# def draw_shape(num_side):
#     for _ in range(num_side):
#         angle=360/num_side
#         tim.right(angle)
#         tim.forward(100)
#
# for num in range(3,11):
#     random_color = randint(1, 255), randint(1, 255), randint(1, 255)
#     screen.colormode(255)
#     tim.pencolor(random_color)
#     draw_shape(num)
# screen.exitonclick()

#------------------draw random walk-----------------#
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_rgb= (r,g,b)
    return random_rgb
screen.colormode(255)
# random_step=random.choice(range(100))
# count=0

# angle=[0,90,180,270]
# tim.width(5)
# while count<50:
#     # random_color = randint(1, 255), randint(1, 255), randint(1, 255)
#     tim.pencolor(random_color())
#     tim.right(random.choice(angle))
#     tim.forward(randint(1,50))
#     count +=1

# ----------------draw spirograph----------------
def draw_circle(num_circle,radius):

    angle=360/num_circle
    for _ in range(num_circle):
        tim.pencolor(random_color())
        tim.speed("fastest")
        tim.circle(radius)
        tim.left(angle)
draw_circle(100,100)
screen.exitonclick()