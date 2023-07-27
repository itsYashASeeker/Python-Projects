import time
from turtle import Screen
from snake import Snake
from food import Food
from scorecard import ScoreCard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

score_c = ScoreCard()
food = Food()
snake = Snake()


screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score_c.add_score()
        snake.extend()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score_c.high_sc()
        snake.new_snake()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 11:
            score_c.high_sc()
            snake.new_snake()

screen.exitonclick()

