from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_WIDTH_BORDER = SCREEN_WIDTH // 2 - 20
SCREEN_HEIGHT_BORDER = SCREEN_HEIGHT // 2 - 20

game_screen = Screen()
game_screen.bgcolor("black")
game_screen.title("Ping Pong Py")
game_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
game_screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

game_screen.listen()
game_screen.onkey(right_paddle.up, "Up")
game_screen.onkey(right_paddle.down, "Down")
game_screen.onkey(left_paddle.up, "w")
game_screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # collision with wall
    if ball.ycor() > SCREEN_HEIGHT_BORDER or ball.ycor() < -SCREEN_HEIGHT_BORDER:
        ball.bounce_floors()

    # collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > SCREEN_WIDTH_BORDER - 60) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -SCREEN_WIDTH_BORDER + 60):
        ball.bounce_paddle()

    if ball.xcor() > SCREEN_WIDTH_BORDER:
        ball.create_ball()
        ball.bounce_paddle()
        score.increase_score(left_paddle)

    if ball.xcor() < -SCREEN_WIDTH_BORDER:
        ball.create_ball()
        ball.bounce_paddle()
        score.increase_score(right_paddle)

game_screen.exitonclick()
