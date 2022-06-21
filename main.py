from turtle import Turtle, Screen
from boards import Boards
from textscreen import Textscreen
from ball import Ball

import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

boards = Boards()
textscreen = Textscreen()
ball = Ball()


screen.listen()
screen.onkeypress(boards.upright, "Up")
screen.onkeypress(boards.upleft, "w")
screen.onkeypress(boards.downright, "Down")
screen.onkeypress(boards.downleft, "s")


game_running = True
left_score = 0
right_score = 0;

while game_running:
    screen.update()
    ball.move()
    if ball.losingcollision():
        game_running = False
        textscreen.gameovermessage()
    if abs(boards.list_boards[1].xcor() - ball.xcor()) < 10 and abs(boards.list_boards[1].ycor() - ball.ycor()) < 40:
        ball.changedirection()
        ball.increasespeed()
        right_score += 1
        textscreen.scoredraw(right_score, left_score)
    if abs(boards.list_boards[0].xcor() - ball.xcor()) < 10 and abs(boards.list_boards[0].ycor() - ball.ycor()) < 40:
        ball.changedirection()
        ball.increasespeed()
        left_score += 1
        textscreen.scoredraw(right_score, left_score)

    time.sleep(0.00001)
screen.exitonclick()