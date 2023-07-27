import random
from turtle import Turtle, Screen
from cars import Car

is_on = True
screen = Screen()
screen.setup(900, 600)
car_list = []

def move_fun():
    while is_on:
        car_list[random.randint(0, 4)].forward(random.randint(50, 150))

for i in range(5):
    car = Car()
    car.speed(random.randint(1, 7))
    car_list.append(car)
move_fun()
screen.exitonclick()
