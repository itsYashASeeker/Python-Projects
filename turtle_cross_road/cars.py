import turtle
import random


class Car(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.shapesize(1, 2)
        self.shap_colo()
        self.goo_position()

    def shap_colo(self):
        turtle.colormode(255)
        r = random.randint(0, 254)
        g = random.randint(0, 254)
        b = random.randint(0, 254)
        self.color(r, g, b)

    def goo_position(self):
        y_co = random.randint(-200, 200)
        x_co = 430
        self.goto(x_co, y_co)
        self.showturtle()


