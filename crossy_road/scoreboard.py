from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Arial", 18, "normal")
BIGFONT = ("Courrier", 96, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-310, 210)
        self.score_view()

    def score_view(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


