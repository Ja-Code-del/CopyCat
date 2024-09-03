from turtle import Turtle
import random
from scenery import COLORS

STARTING_COR = [(-320, -190), (-320, -160), (-320, -130),
                (-320, -100), (-320, -70), (-320, -40), (-320, -10),
                (-320, 20), (-320, 50), (-320, 80), (-320, 110),
                (-320, 140), (-320, 170)]

STARTING_POSITIONS = (-320, -190)


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cameleo = random.choice(COLORS)
        self.compartment = []
        self.car_mode = random.randint(1, 4)
        self.penup()
        self.shape("square")
        self.color(self.cameleo)
        self.goto(-300, -190)



    def run(self):
        

