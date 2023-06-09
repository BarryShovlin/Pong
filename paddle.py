from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def starting_pos(self, x_y_cor):
        self.goto(x_y_cor)

    def move_up(self):
        new_ycor = self.ycor() + 20
        self.sety(new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.sety(new_ycor)