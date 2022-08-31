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
