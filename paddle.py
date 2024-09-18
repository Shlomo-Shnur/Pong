from turtle import Turtle

MOVEMENT = 20
START_POSITION_X_RIGHT = 350
START_POSITION_X_LEFT = -350
START_POSITION_Y = 0


def up(paddle):
    new_ycor = paddle.ycor() + MOVEMENT
    paddle.goto(paddle.xcor(), new_ycor)


def down(paddle):
    new_ycor = paddle.ycor() - MOVEMENT
    paddle.goto(paddle.xcor(), new_ycor)


class Paddle:

    def __init__(self):
        self.left_paddle = Turtle()
        self.right_paddle = Turtle()
        self.create_paddles()

    def create_paddles(self):
        position_right = (START_POSITION_X_RIGHT, START_POSITION_Y)
        position_left = (START_POSITION_X_LEFT, START_POSITION_Y)
        self.right_paddle.color("white")
        self.left_paddle.color("white")
        self.right_paddle.shape("square")
        self.left_paddle.shape("square")
        self.right_paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.left_paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.right_paddle.penup()
        self.left_paddle.penup()
        self.right_paddle.goto(position_right)
        self.left_paddle.goto(position_left)
