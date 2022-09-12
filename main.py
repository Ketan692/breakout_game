from turtle import *
import random
from blocks import Block
from paddle import Paddle
from ball import Ball
import time


tim = Turtle()
screen = Screen()
screen.setup(width=900, height=750, startx=10, starty=10)
screen.bgcolor("black")

VERTICAL_LIMIT = 385
HORIZONTAL_LIMIT = 400


screen.tracer(0)
paddle = Paddle()

screen.listen()
ball = Ball()
screen.onkey(fun=paddle.lf, key="Left")
screen.onkey(fun=paddle.rg, key="Right")

x = -370
y = 330
lenght = 4
colors = ["Green", "Blue", "Orange", "Violet", "Red"]
positions = []

for i in range(28):
    enemy = Block()
    enemy.color(random.choice(colors))
    if x >= 370:
        x = -370
        y -= 60
    enemy.goto(x, y)
    if lenght == 4:
        enemy.shapesize(stretch_wid=2, stretch_len=lenght)
        lenght = 6
    elif lenght == 6:
        enemy.shapesize(stretch_wid=2, stretch_len=lenght)
        lenght = 4
    x += 120
    screen.update()
    positions.append(enemy)

is_game_on = True
while is_game_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    # Detect Collision with ceiling
    if ball.ycor() > VERTICAL_LIMIT:
        ball.bounce_y()

    # Detect Collision with side walls
    if ball.xcor() > HORIZONTAL_LIMIT+20 or ball.xcor() < -HORIZONTAL_LIMIT-20:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 45 and ball.ycor() < 290:
        ball.bounce_y()

    # Detect collision with brick
    for brick in positions:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            brick.hideturtle()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                ball.bounce_x()
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                ball.bounce_x()
                ball.bounce_y()
            positions.remove(brick)
            break

    # Detect paddle miss
    if ball.ycor() < -VERTICAL_LIMIT:
        is_game_on = False

    if not positions:
        is_game_on = False

update()


















screen.mainloop()