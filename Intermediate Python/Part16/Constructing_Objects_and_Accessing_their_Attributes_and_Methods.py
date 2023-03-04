import turtle as tr #turtle is a prebuilt module

timmy=tr.Turtle() #from the turtle module we are importing the Turtle class and using it to create a object from it
#print(timmy) #it is an object of the class Turtle
timmy.shape('turtle') # changes the shape of the turtle
timmy.color('Red') #chaging the color of the turtle
timmy.forward(100) #moves the turtle forward
my_screen=tr.Screen() #it is the screen on which the turtle object is going to show up

print(my_screen.canvheight)  #prints the height for the screen created

my_screen.exitonclick() 
# as the turtle object is created it opens up whenever the program runs
#its canvas height is determined by the attribute canvheight
print(type(timmy)) #shos from where the object is comming
print(tr) #while seeing the type of a funtion brackets should be avoided
