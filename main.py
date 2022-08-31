from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

is_game_on = True
while is_game_on:

    screen.listen()
    screen.onkey(snake.up, 'w')
    screen.onkey(snake.left, 'a')
    screen.onkey(snake.down, 's')
    screen.onkey(snake.right, 'd')
    screen.update()
    time.sleep(0.075)
    score.print_score()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.eaten()
        score.increment()

    if snake.head.xcor() > 280 or snake.head.xcor() < -285\
            or snake.head.ycor() > 280 or snake.head.ycor() < -280\
            or snake.has_bite_itself():
        is_game_on = False
        score.game_over()

screen. exitonclick()
