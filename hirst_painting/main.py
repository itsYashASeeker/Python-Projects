# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# rgb_color=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
import turtle
import random

tim = turtle.Turtle()
rgb_color = [(226, 231, 236), (57, 107, 148), (224, 200, 110), (134, 85, 59), (222, 140, 64), (195, 145, 171),
             (234, 225, 202), (145, 179, 203), (223, 233, 229), (138, 82, 106), (209, 91, 68), (187, 80, 120),
             (134, 182, 136), (69, 104, 89), (236, 222, 230), (66, 155, 90), (50, 155, 194), (131, 133, 75),
             (183, 192, 201), (213, 178, 192), (21, 68, 112), (20, 59, 94), (116, 124, 147), (226, 176, 167),
             (175, 202, 183), (159, 206, 215), (70, 60, 48), (138, 41, 35), (74, 65, 50), (53, 72, 67)]
turtle.colormode(255)
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)


def go_on():
    for i in range(10):
        tim.dot(20, random.choice(rgb_color))
        tim.forward(50)
    tim.back(50)


for i in range(5):
    go_on()
    tim.left(90)
    tim.forward(50)
    tim.left(90)

    go_on()
    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen = turtle.Screen()
screen.exitonclick()
