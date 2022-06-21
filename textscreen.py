from turtle import Turtle

class Textscreen(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.ht()
        self.right(90)
        self.width(5)
        self.drawline()
        self.scoredraw(0, 0)

    def gameovermessage(self):
        self.goto(0, 0)
        self.write("Game Over", True, "center", ('Arial', 25, 'normal'))


    def drawline(self):
        self.goto(0, 300)
        for n in range(0, 8):
            self.pendown()
            self.forward(50)
            self.penup()
            self.forward(50)

    def scoredraw(self, scoreright, scoreleft):
        self.clear()
        self.drawline()
        self.goto(50, 220)
        self.write(f"{scoreright}", True, "center", ('Arial', 50, 'normal'))
        self.goto(-50, 220)
        self.write(f"{scoreleft}", True, "center", ('Arial', 50, 'normal'))

