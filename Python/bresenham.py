#Bresenham's Line Drawing Algorithm

#In this,x1,y1 should be less than x2,y2 and m<1
import turtle as t

x1 = float(input("x-coordinate: "))
y1 = float(input("y-coordinate: "))

x2 = float(input("x-coordinate: "))
y2 = float(input("y-coordinate: "))

dx = x2 - x1
dy = y2 - y1
screen = t.Screen()

p = t.Turtle()
p.shapesize(0.3)

p.speed("fastest")
p.shape("circle")

e = 2*dy - dx

p.penup()
p.goto(int(x1), int(y1))
p.pendown()

for i in range(int(dx)):
    x1 += 1
    if e < 0:
        e += 2*dy

    else:
        e += 2 * dy - 2 * dx
        y1 += 1

    p.goto(int(x1), int(y1))

screen.exitonclick()
