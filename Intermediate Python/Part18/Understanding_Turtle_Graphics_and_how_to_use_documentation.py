#Turtle Graphics Documentation:   https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

timmy=Turtle()

#same as import turtle as tr
#timmy=tr.turtle()
#all the methods and attributes of the Turtle class therefore
#can be handled without referencing the module (turtle)
#in-order to keep the turtle showup in the screen another object of the screen class needs to be created

timmy.shape("turtle")
timmy.color("dim gray")
timmy.color("red")
timmy.forward(100) #moving the turtle forward by 100 spaces
timmy.right(90) #the right method takes an angle as an input
















screen=Screen()
screen.exitonclick() #to preview the turtle