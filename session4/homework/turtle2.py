from turtle import*

import turtle

speed = 0

colors = ("red", "blue", "brown", "yellow", "grey")

for i, color in enumerate(colors):

    begin_fill()

    turtle.color(color)
    for i in range (2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward (50)

    end_fill()

mainloop()
