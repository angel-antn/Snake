<<<<<<< HEAD
from turtle import Turtle
ALIGN = 'center'
FONT = ('Consolas', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.score = 0
        self.color('white')

        try:
            file = open('high_score.dat', 'r')
        except FileNotFoundError:
            file = open('high_score.dat', 'w')
            file.write('0')
            file.close()
            file = open('high_score.dat', 'r')

        self.high_score = int(file.read())
        file.close()

    def increment(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def print_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score} // High Score: {self.high_score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='GAME OVER', align=ALIGN, font=FONT)

    def update_high_score(self):
        if self.high_score == self.score:
            with open("high_score.dat", mode="w") as file:
                file.write(str(self.high_score))
                self.goto(x=0, y=-20)
                self.write(arg='NEW HIGH SCORE!', align=ALIGN, font=FONT)
=======
from turtle import Turtle
ALIGN = 'center'
FONT = ('Consolas', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.score = 0
        self.color('white')

    def increment(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='GAME OVER', align=ALIGN, font=FONT)
>>>>>>> 4d27b43c4882086c218f83a99bf471b8a628f709
