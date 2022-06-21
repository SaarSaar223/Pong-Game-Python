from turtle import Turtle
import random



class Ball(Turtle):
    Up = True
    Right = True
    Speed = 1
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        self.speed("fastest")
        self.move()

    def move(self):
        if self.wallcollision():
            Ball.Up = not Ball.Up

        if Ball.Up:
            ypos = self.ycor() + 1
        else:
            ypos = self.ycor() - 1

        if Ball.Right:
            xpos = self.xcor() + Ball.Speed
        else:
            xpos = self.xcor() - Ball.Speed

        self.goto(xpos, ypos)

    def losingcollision(self):
        if self.xcor() >= 383 or self.xcor() <= -383:
            return True

    def wallcollision(self):
        if self.ycor() >= 283 or self.ycor() <= -283:
            return True

    def changedirection(self):
        Ball.Right = not Ball.Right

    def increasespeed(self):
        Ball.Speed += 0.5