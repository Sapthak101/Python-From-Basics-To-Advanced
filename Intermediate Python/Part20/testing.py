from turtle import Screen, Turtle

FONT = ('Arial', 16, 'normal')

def write_text(center_x, center_y, text):
    ''' Write text on the Screen '''

    board.penup()
    board.goto(center_x, center_y)
    board.write(text, font=FONT)

board = Turtle()

write_text(100, 100, "You are here.")

screen = Screen()
screen.exitonclick()