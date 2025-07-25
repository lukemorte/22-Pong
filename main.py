from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, BALL_SIZE

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
screen.onkeypress(key="w", fun=l_paddle.moveup)
screen.onkeypress(key="s", fun=l_paddle.movedown)
screen.onkeypress(key="Up", fun=r_paddle.moveup)
screen.onkeypress(key="Down", fun=r_paddle.movedown)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    # detect collision with a wall
    if ball.ycor() > (SCREEN_HEIGHT // 2) - BALL_SIZE or ball.ycor() < (-SCREEN_HEIGHT // 2) + BALL_SIZE:
        ball.bounce_y()

    # detect collision with a right paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 100 or ball.xcor() < -320 and ball.distance(l_paddle) < 100:
        ball.bounce_x()


screen.exitonclick()
