from turtle import Screen, Turtle
import time
from Food import food
from Scoreboard import scoreboard

STARTING_POSITIONS=[(0,0), (-20,0), (-40,0)]
ALLIGNMENT = "center"
FONT=("Arial", 24, "normal")

class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.head=self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.turtles.append(new_segment)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for seg_num in range(len(self.turtles) -1, 0 ,-1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
f1=food()
s1=scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update() #used to control the flow of animations, refreshing screen
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(f1) < 15:
        f1.refresh()
        snake.extend()
        s1.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        s1.game_over()
        game_is_on=False

    for turtle in snake.turtles:
        if turtle == snake.head:
            pass
        elif snake.head.distance(turtle)<16:
            game_is_on=False
            s1.game_over()

screen.exitonclick()