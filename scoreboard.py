from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        if player.xcor() > 0:
            self.right_score += 1
        else:
            self.left_score += 1
        self.write_score()

    def game_over(self):
        self.home()
        self.write(f"Game Over.", align=ALIGNMENT, font=FONT)
