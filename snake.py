from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            snake_part = Turtle(shape='square')
            snake_part.color('white')
            snake_part.penup()
            snake_part.goto(x=0+i*-20, y=0)
            self.snake.append(snake_part)
        self.head = self.snake[0]

    def eaten(self):
        snake_part = Turtle(shape='square')
        snake_part.color('white')
        snake_part.penup()
        snake_part.setposition(self.snake[-1].pos())
        self.snake.append(snake_part)

    def has_bite_itself(self):
        for i in self.snake[1:]:
            if i.distance(self.head) < 10:
                return True
        return False

    def move(self):
        for i in range(1, len(self.snake)):
            self.snake[-i].goto(self.snake[-(i + 1)].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
