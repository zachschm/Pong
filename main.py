import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
WIN = 4
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
# Paddle and ball creation
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()
# Event listeners
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
# Boolean to control game status
game_is_on = True
# Game Program
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Checks if ball hits top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Checks if ball hits a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()
    # check if player has scored
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()
    # Checks if player has scored
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()
    # Ensures game point
    if score.l_score > WIN or score.r_score > WIN:
        score.over()
        game_is_on = False

screen.exitonclick()