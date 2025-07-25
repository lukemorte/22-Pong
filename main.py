from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR

# class: Playground
# class: Paddle
# class: Ball
# class: Score

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(key="w", fun=l_paddle.moveup)
screen.onkey(key="s", fun=l_paddle.movedown)
screen.onkey(key="Up", fun=r_paddle.moveup)
screen.onkey(key="Down", fun=r_paddle.movedown)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()


screen.exitonclick()
