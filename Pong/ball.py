from turtle import Turtle

INITIAL_ANGLE = 300


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(180, 180, 180)
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.penup()
        self.angle = INITIAL_ANGLE
        self.velocity = 5

    def move(self):
        self.setheading(self.angle)
        self.forward(self.velocity)
        if self.ycor() > 220:
            self.setheading(360 - self.angle)
            self.angle = self.heading()
            self.forward(self.velocity)
        elif self.ycor() < -220:
            self.setheading(360 - self.angle)
            self.angle = self.heading()
            self.forward(self.velocity)
        else:
            self.forward(self.velocity)
