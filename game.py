from turtle import Screen
from paddle import Paddle, up, down
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_WIDTH_BORDER = SCREEN_WIDTH // 2 - 20
SCREEN_HEIGHT_BORDER = SCREEN_HEIGHT // 2 - 20


def game():
    game_screen = Screen()
    game_screen.bgcolor("black")
    game_screen.title("Ping Pong Py")
    game_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    game_screen.tracer(0)

    paddles = Paddle()
    ball = Ball()
    score = Scoreboard()

    game_screen.listen()
    game_screen.onkey(lambda: up(paddles.right_paddle), "Up")
    game_screen.onkey(lambda: down(paddles.right_paddle), "Down")
    game_screen.onkey(lambda: up(paddles.left_paddle), "w")
    game_screen.onkey(lambda: down(paddles.left_paddle), "s")

    game_is_on = True
    while game_is_on:
        game_screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # collision with wall
        if ball.ycor() > SCREEN_HEIGHT_BORDER or ball.ycor() < -SCREEN_HEIGHT_BORDER:
            ball.bounce_floors()

        # collision with paddles
        if (ball.distance(paddles.right_paddle) < 50 and ball.xcor() > SCREEN_WIDTH_BORDER - 60) or \
                (ball.distance(paddles.left_paddle) < 50 and ball.xcor() < -SCREEN_WIDTH_BORDER + 60):
            ball.bounce_paddle()

        if ball.xcor() > SCREEN_WIDTH_BORDER:
            ball.create_ball()
            ball.bounce_paddle()
            score.increase_score(paddles.left_paddle)

        if ball.xcor() < -SCREEN_WIDTH_BORDER:
            ball.create_ball()
            ball.bounce_paddle()
            score.increase_score(paddles.right_paddle)

    game_screen.exitonclick()


if __name__ == "__main__":
    game()
