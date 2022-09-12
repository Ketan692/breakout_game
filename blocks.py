from turtle import Turtle


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.penup()

