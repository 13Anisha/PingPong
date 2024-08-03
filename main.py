from turtle import Screen
from paddle import Paddle
from table import Table
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
table = Table()
ball = Ball()
score_left = Score((-100, 260))
score_right = Score((100, 260))

screen.listen()
screen.onkey(paddle_left.up, "Up")
screen.onkey(paddle_left.down, "Down")
screen.onkey(paddle_right.up, "Left")
screen.onkey(paddle_right.down, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Detect collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Detect collision with right wall
    if ball.xcor() > 380:
        ball.refresh()
        score_left.update()

    # Detect collision with left wall
    if ball.xcor() < -380:
        ball.refresh()
        score_right.update()

screen.exitonclick()
