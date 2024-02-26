from turtle import Screen, Turtle
import time 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []

#set up 3-segment snake
starting_positions = [0, -20, -40]
for i in starting_positions:
    turtle1 = Turtle("square")
    turtle1.color('white')
    turtle1.penup()
    turtle1.setposition(x=i, y=0)
    segments.append(turtle1)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)
        






screen.exitonclick()