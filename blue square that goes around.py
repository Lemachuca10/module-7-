#Luis Machcua
#2/28/2020
#In this program it will show a blue spiral square and the background color is lightgreen.
import turtle
def drawSquare(t,side):
  for i in range(4):
      t.forward(side)
      t.left(90)
wn = turtle.Screen()
wn.bgcolor("lightblue")
Machuca = turtle.Turtle()
Machuca.speed(2)
Machuca.pencolor("blue")
mv = -10
for sq in range(20,101,20):
  drawSquare(Machuca,sq)
  Machuca.penup()
  Machuca.goto(mv,mv)
  Machuca.pendown()
  mv = mv -10
wn.exitonclick()
