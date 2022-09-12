import turtle
from turtle import *

turtle.title("Gabriela Pardo - Python Turtle")
speed(10000000000000)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    fd(50+i)
    rt(91)
    pencolor(r,g,b)

t=turtle.Turtle()
t.penup()

t.goto(-400,50)
t.pendown()
t.pensize(10)
t.pencolor("red")

t.right(90)
t.forward(150)

t.right(-90)
t.forward(70)

t.penup()

t.goto(-300,50)
t.pendown()
t.pensize(10)
t.pencolor("red")

t.right(90)
t.forward(150)

t.penup()

t.goto(-30,50)
t.pendown()
t.pensize(10)
t.pencolor("red")

t.right(90)
t.forward(150)

t.goto(-30,50)
t.goto(50,-90)
t.goto(50,50)


t.penup()

t.goto(300,50)
t.pendown()
t.pensize(10)
t.pencolor("red")

t.right(65)
t.forward(-100)

t.setpos(300,50)
t.right(50)
t.forward(-100)

t.penup()
t.setpos(300,-10)
t.right(65)
t.pendown()
t.backward(50)