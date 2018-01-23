from turtle import*

shape("turtle")

speed(0)


def triangle():
    for i in range(3):
        forward(100)
        left(360 / 3)
def square():
   for i in range(4):
       forward(100)
       left(360 / 4)
def pentagon():
   for i in range(5):
       forward(100)
       left(360 / 5)
def hexagon():
   for i in range(6):
       forward(100)
       left(360 / 6)

def pentagon():
    for i in range (7):
        forward(100)
        left


color("red")
triangle()

color("brown")
pentagon()

color("blue")
square()

color("yellow")
hexagon()




mainloop()
