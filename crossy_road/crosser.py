from turtle import Turtle

INITIAL_POSITION = (0, -320)


class Crosser(Turtle):
    """The crosser class"""

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("gray")
        self.penup()
        self.goto(INITIAL_POSITION)


