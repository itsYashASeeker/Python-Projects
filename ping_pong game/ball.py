from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.num_of_steps = 1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        if self.heading() < 90:
            zx = self.num_of_steps
            zy = self.num_of_steps
        elif self.heading() < 180:
            zx = -self.num_of_steps
            zy = self.num_of_steps
        elif self.heading() < 270:
            zx = -self.num_of_steps
            zy = -self.num_of_steps
        else:
            zx = self.num_of_steps
            zy = -self.num_of_steps
        x = self.xcor() + zx
        y = self.ycor() + zy
        self.goto(x, y)

    def reset_pos_r(self):
        self.goto(0, 0)
        self.setheading(180)
        self.num_of_steps = 1

    def reset_pos_l(self):
        self.goto(0, 0)
        self.setheading(0)
        self.num_of_steps = 1
