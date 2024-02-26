from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#set up 3-segment snake
starting_positions = [0, -20, -40]
for i in starting_positions:
    turtle1 = Turtle("square")
    turtle1.color('white')
    turtle1.setposition(x=i, y=0)







screen.exitonclick()