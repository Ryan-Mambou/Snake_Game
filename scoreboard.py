from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            high_score = file.read()
            self.high_score = int(high_score)
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()

    def update_high_score(self):
        with open('high_score.txt', mode='w') as file:
            # file.truncate(0)
            file.write(f"{self.score}")

