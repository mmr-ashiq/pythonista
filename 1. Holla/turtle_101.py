# https://youtu.be/_FxzEAIWvtE

import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)


# turtle is a module. turtle.Pen is a class. t is an object.
# t is an instance of the class Pen. t is an instance of the module turtle.
