from turtle import Turtle, Screen

INITIAL_POSITION = (-10, -190)
RIGHT = 0
LEFT = 180
UP = 90
MINIMAL_DISTANCE = 30

screen = Screen()


class Crosser(Turtle):
    """The crosser class"""

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("gray")
        self.penup()
        self.goto(INITIAL_POSITION)
        self.forward(MINIMAL_DISTANCE)

    def go_up(self):
        self.setheading(UP)
        self.forward(MINIMAL_DISTANCE)

    def go_left(self):
        self.setheading(LEFT)
        self.forward(MINIMAL_DISTANCE)

    def go_right(self):
        self.setheading(RIGHT)
        self.forward(MINIMAL_DISTANCE)

    def move(self):
        screen.onkeypress(self.go_up, "Up")
        screen.onkeypress(self.go_left, "Left")
        screen.onkeypress(self.go_right, "Right")
