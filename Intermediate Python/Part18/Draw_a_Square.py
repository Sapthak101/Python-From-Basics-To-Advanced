from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")

for number in range(0,4):
    timmy.forward(100)
    timmy.left(90)

screen=Screen()
screen.exitonclick()

#to import everything from a module use * similar representation is done in the other documentation too
#to import a module use pip install module_name for the Visula Studio Code
#to do it in Pycharm in an easier way write the module name and then a red bulb appear on top of the mdoule you want to install but
#it is not available then click on that and install the package
