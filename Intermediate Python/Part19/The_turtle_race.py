from turtle import Turtle, Screen
import random


screen=Screen()

screen.setup(width=500, height=400)
user_text=screen.textinput(title="Make your choice", prompt="Which turtle will win the race? Enter a color: ")
user_text=user_text.lower()
colors=["red", "orange", "yellow", "green", "blue", "purple"]
y_positions=[-70,-40, -10, 20, 50, 80]

is_race_on=False
if user_text:
    is_race_on=True

all_turtles=[]

for turtle_index in range(0,6):
    timmy=Turtle()
    timmy.shape("turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])
    timmy.goto(x=-238, y=y_positions[turtle_index])
    all_turtles.append(timmy)

while is_race_on :
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_text:
                print(f"You have predicted correctly. Turtle {user_text} has won the race")
            else:
                print(f"Your prediction is incorrect. The winner is Turtle {winning_color}")
        rand_distance=random.randint(0,100)
        width=turtle.forward(rand_distance)


screen.exitonclick()