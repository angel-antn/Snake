<<<<<<< HEAD
from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-270, 280))
=======
from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
>>>>>>> 4d27b43c4882086c218f83a99bf471b8a628f709
