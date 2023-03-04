import turtle as t
import random

timmy=t.Turtle()
t.colormode(255) #selecting th rgb max value

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)

    random_color1 =(r,g,b)

    return random_color1

timmy.speed("fastest")
def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):   
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap) #by default east=0, north=90, west=180, south=270
 
spirograph(1) 
screen=t.Screen()
screen.exitonclick()