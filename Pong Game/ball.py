from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # These positions will only be taken once. i.e. at the beginning
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def movement(self):
        new_x = (self.xcor()) + self.x_move
        new_y = (self.ycor()) + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = -self.y_move
        print(self.move_speed)

    def bounce_x(self):
        self.x_move = -self.x_move
        print(self.move_speed)

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05

    # def speed_increase(self):
    #     self.x_move += 2
    #     self.y_move += 2
