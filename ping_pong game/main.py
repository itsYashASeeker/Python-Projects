import time
import turtle

from score import Score
from turtle import Screen
from slits import Slits
from divider import Divider
from ball import Ball

hit = False
is_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
l_slit = Slits((-350, 0))
r_slit = Slits(( 350, 0))
div = Divider()
ball = Ball()
score = Score()
screen.tracer(1)
welcome = screen.textinput("Pong Game", "Hello! Welcome to multiplayer ping-pong game!! Are you ready??")
left = screen.textinput("Pong game", "What's your name?(left)--(w-s key)").lower().capitalize()
right = screen.textinput("Pong game", "What's your name?(right)--(up-down key)").lower().capitalize()
screen.listen()

screen.onkey(r_slit.up, "Up")
screen.onkey(r_slit.down, "Down")
screen.onkey(l_slit.up, "w")
screen.onkey(l_slit.down, "s")


def hit_wall():
    if ball.ycor()>290:
        if ball.heading() < 90 :
            ball.setheading(ball.heading() - 90)
        else:
            ball.setheading(ball.heading()+90)
    elif ball.ycor()<-290:
        if ball.heading()<270:
            ball.setheading(ball.heading()-90)
        else:
            ball.setheading(ball.heading()+90)


def hit_slide():
    if ball.heading() > 90 and ball.heading() < 180:
        angle_of_dir = -90
    elif ball.heading() >270:
        angle_of_dir =-90
    else:
        angle_of_dir = 90
    if ball.distance(r_slit) < 52 and ball.xcor() > 340:
        ball.setheading(ball.heading()+angle_of_dir)
        ball.num_of_steps += 0.1
    elif ball.distance(l_slit) < 52 and ball.xcor() < -340:
        ball.setheading(ball.heading()+angle_of_dir)
        ball.num_of_steps += 0.1


def is_winner():
    global is_on
    if score.l_score == 5:
        turtle.color("red")
        turtle.write(left+" Wins!!",align="center", font=("arial", 40, "normal"))
        is_on = False
    elif score.r_score == 5:
        turtle.color("red")
        turtle.write(right+" Wins!!", align="center", font=("arial", 40, "normal"))
        is_on = False

screen.tracer(0)
while is_on:
    screen.update()
    ball.move()
    hit_slide()
    hit_wall()
    if ball.xcor() > 370:
        ball.reset_pos_r()
        score.l_point()
    elif ball.xcor() < -370:
        ball.reset_pos_l()
        score.r_point()
    is_winner()

screen.exitonclick()