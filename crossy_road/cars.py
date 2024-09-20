import turtle
from turtle import Turtle
import random
from scenery import COLORS

STARTING_COR = [(-320, -190), (-320, -160), (-320, -130),
                (-320, -100), (-320, -70), (-320, -40), (-320, -10),
                (-320, 20), (-320, 50), (-320, 80), (-320, 110),
                (-320, 140), (-320, 170)]

STARTING_POSITIONS = (-320, -190)


class Cars(Turtle):
    def __init__(self, numb_of_car):
        super().__init__()
        self.cars = []
        self.available_velocity = random.sample(range(1, 15), numb_of_car)
        for _ in range(numb_of_car):
            self.creation()

    def creation(self):
        car = Turtle("square")
        col = random.choice(COLORS)
        car.penup()
        car.color(col)
        car.goto(random.choice(STARTING_COR))
        velocity = self.available_velocity.pop()
        self.cars.append((car, velocity))

    def run(self):
        for car, velocity in self.cars:
            car.forward(velocity)
            if car.xcor() > 320:
                car.goto(-320, car.ycor())  # Réinitialiser la position à gauche
                new_velocity = random.choice(range(2, 10))  # Nouvelle vitesse aléatoire
                self.cars[self.cars.index((car, velocity))] = (car, new_velocity)  # Mettre à jour la vitesse