from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.goto(x=0, y=-330)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_cor = self.xcor()+self.x_move
        y_cor = self.ycor()+self.y_move
        self.goto(x=x_cor, y=y_cor)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
