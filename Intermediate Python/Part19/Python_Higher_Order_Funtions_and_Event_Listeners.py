from turtle import Turtle, Screen

timmy=Turtle()
screen=Screen()

def move_forward():
    timmy.forward(10)

screen.listen() #to interpret the user command in the GUI
screen.onkey(key="space", fun=move_forward) #binds a funtion to perform a specific task and the function passed should not have any parentheses and it should be paramterless

screen.exitonclick()
# a function that takes other function as an input is called a higher order function
#thery not compartible with the builtin funtions

#giving only the funtion means we have given the funtion as an input
#giving a funtion along with its arguments means that the function inputted is first evaluated then its output is given as an input to the other funtion 