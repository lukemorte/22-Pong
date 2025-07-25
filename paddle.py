from turtle import Turtle
from constants import PADDLE_MOVEMENT


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def moveup(self):
        new_y = self.ycor() + PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)

    def movedown(self):
        new_y = self.ycor() - PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)
