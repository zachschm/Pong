from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 90, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 90, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 90, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 90, "normal"))

    # Adds point to the left player
    def l_point(self):
        self.l_score += 1
        self.update_score()

    # Adds point to the right player
    def r_point(self):
        self.r_score += 1
        self.update_score()

    # Game over message and feedback
    def over(self):
        self.goto(0, 40)
        self.write("Game Over", align="center", font=("Courier", 60, "normal"))
        self.goto(0, -40)
        if self.l_score > self.r_score:
            self.write("Left Player Wins", align="center", font=("Courier", 60, "normal"))

        else:
            self.write("Right Player Wins", align="center", font=("Courier", 60, "normal"))





