import turtle as t

timmy=t.Turtle()

def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

screen=t.Screen()
screen.exitonclick()