from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",17,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",17,"normal"))

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update()
