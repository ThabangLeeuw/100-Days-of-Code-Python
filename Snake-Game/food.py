from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Yellow")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        food_position_x = randint(-280, 280)
        food_position_y = randint(-280, 280)
        self.goto(food_position_x, food_position_y)