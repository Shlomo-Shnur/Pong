from turtle import Turtle

MOVEMENT = 20
START_POSITION_X = 350
START_POSITION_Y = 0


class Paddle(Turtle):

    def __init__(self, position=0):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position=0):
        if not position:
            position = (START_POSITION_X, START_POSITION_Y)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_ycor = self.ycor() + MOVEMENT
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - MOVEMENT
        self.goto(self.xcor(), new_ycor)
