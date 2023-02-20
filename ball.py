from turtle import Turtle
SLEEP = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    # Properly moves ball througout the program
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    # If the top or bottom wall is hit, the y motion is flipped
    def bounce_y(self):
        self.y_move *= -1

    # If the side wall is hit, the x motion is flipped
    def bounce_x(self):
        self.x_move *= -1

    # Resets ball location, direction, and speed
    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        self.reset_speed()

    # Increases the speed of the ball
    def speed_up(self):
        self.move_speed *= 0.9

    # Resets the speed of the ball to starting speed
    def reset_speed(self):
        self.move_speed = SLEEP



