from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")

for number in range(0,10):
    timmy.forward(10)
    timmy.penup() #no visible mark will be made
    timmy.forward(10)
    timmy.pendown()


screen=Screen()
screen.exitonclick()
