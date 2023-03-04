my_tuple=(1,2,3)
#tuples cannot be appended, modified
print(my_tuple[0])
#used to avoid accidental change in data
# a tuple can converted into a list by putting it into the ;ist function

list1=list(my_tuple)

#changing the color mode from the turtle class static data member
import turtle as t
import random

t.colormode(255) #selecting th rgb max value
def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)

    random_color1 =(r,g,b)

    return random_color1

timmy=t.Turtle()
timmy.color(random_color())

screen=t.Screen()
screen.exitonclick()