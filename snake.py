from turtle import Turtle
STARTING=[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create()
        self.head=self.segments[0]

    def create(self):
        for i in STARTING:
            self.add_seg(i)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        self.head.forward(MOVE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_seg(self,pos):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(pos)
        self.segments.append(new_snake)

    def extend(self):
        self.add_seg(self.segments[-1].position())
