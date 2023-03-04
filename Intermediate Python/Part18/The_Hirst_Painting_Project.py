#pip install colorgram.py
import colorgram
colors=colorgram.extract("images.jpg", 30)
print(colors)
rgb_colors=[]
for color in colors:
    r=color.rgb.r #to extract a particular r value
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color) #assigns the rgb value to the list as a tuple
print(rgb_colors)

import turtle
from random import choice
from turtle import Turtle
turtle.colormode(255)
timmy=Turtle()

timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.hideturtle()

for dot_count in range(1, 101):
    timmy.dot(20, choice(rgb_colors)) #needs to give a rgb tuple as an input
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)  # position not according to a particular position
        timmy.forward(500)
        timmy.setheading(0)

screen=turtle.Screen()
screen.exitonclick()
