from turtle import Turtle, Screen
from random import choice

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions=[0, 90, 180, 270]

timmy.width(10)
timmy.speed(30) #string: "fastest", "fast", "normal", "slow", "slowest" attributes for the speed, or a number
for number in range(0, 100):
    timmy.forward(30)
    timmy.color(choice(colours))
    timmy.setheading(choice(directions))


screen=Screen()
screen.exitonclick()