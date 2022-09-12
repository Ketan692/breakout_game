from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("#fff")
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=8)
        self.goto(x=0, y=-330)

    def lf(self):
        new_x = self.xcor()-20
        self.goto(x=new_x, y=-330)

    def rg(self):
        new_x = self.xcor()+20
        self.goto(x=new_x, y=-330)


