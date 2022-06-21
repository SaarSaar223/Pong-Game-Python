import turtle
from turtle import Turtle, Screen

class Boards():
    list_boards = []

    def __init__(self):
        self.leftboardcreate()
        self.rightboardcreate()




    def rightboardcreate(self):
        rightboard = Turtle("square")
        rightboard.resizemode("user")
        rightboard.color("white")
        rightboard.shapesize(0.5, 4)
        rightboard.left(90)
        rightboard.penup()
        rightboard.goto(370, 0)
        self.list_boards.append(rightboard)
    def leftboardcreate(self):
        leftboard = Turtle("square")
        leftboard.resizemode("user")
        leftboard.color("white")
        leftboard.shapesize(0.5, 4)
        leftboard.penup()
        leftboard.goto(-370, 0)
        leftboard.left(90)
        self.list_boards.append(leftboard)


    def upright(self):
        if self.list_boards[1].ycor() > 250:
            pass
        else:
            self.list_boards[1].forward(10)

    def downright(self):
        if self.list_boards[1].ycor() < -240:
            pass
        else:
            self.list_boards[1].backward(10)

    def upleft(self):
        if self.list_boards[0].ycor() > 250:
            pass
        else:
            self.list_boards[0].forward(10)

    def downleft(self):
        if self.list_boards[0].ycor() < -240:
            pass
        else:
            self.list_boards[0].backward(10)