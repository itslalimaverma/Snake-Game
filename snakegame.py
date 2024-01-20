from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

# screen.exitonclick()
snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inc_score()
    #wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        score.gameover()

    #tail
    for i in snake.segments:
        if i==snake.head:
            pass
        elif snake.head.distance(i)<10:
            game_on=False
            score.gameover()
screen.exitonclick()