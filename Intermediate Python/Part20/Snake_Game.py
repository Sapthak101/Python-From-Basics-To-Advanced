from turtle import Screen, Turtle
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#segment1=Turtle("square")
#segment1.color("white")
#segment2=Turtle("square")
#segment2.color("white")
#segment2.goto((-20, 0))
#segment3=Turtle("square")
#segment3.color("white")
#segment3.goto((-40,0))

#or
turtles=[]
starting_positions=[(0,0), (-20,0), (-40,0)]
for position in starting_positions:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    turtles.append(new_segment)

screen.update()
game_is_on=True 
while game_is_on:
    screen.update() #used to control the flow of animations, refreshing screen     
    time.sleep(0.1) #used to set the tranision between one frame to another
    
    for seg_num in range(2,0,-1):
        new_x=turtles[seg_num-1].xcor()
        new_y=turtles[seg_num-1].ycor()
        turtles[seg_num].goto(new_x, new_y)
    turtles[0].forward(20)
    turtles[0].left(90)
screen.exitonclick()