from turtle import Screen
from ball import Ball
import time
from scoreboard import Scoreboard

from paddle import Paddle

screen = Screen()
screen.screensize(800, 600, "black")
screen.title("The Pong Game")
screen.tracer(0)

paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-360, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(paddle_1.go_up, "w")
screen.onkeypress(paddle_1.go_down, "s")
screen.onkeypress(paddle_2.go_up, "Up")
screen.onkeypress(paddle_2.go_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 325 or ball.distance(paddle_2) < 50 and ball.xcor() < -335:
        ball.bounce_x()
        ball.move_speed *= 0.9
        # ball.speed_increase()
        print("Made contact")
        print(ball.move_speed)

    if ball.xcor() > 355:
        ball.ball_reset()
        score.l_point()

    if ball.xcor() < -365:
        ball.ball_reset()
        score.r_point()


screen.exitonclick()
