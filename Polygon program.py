#Luis Machuca
#2/28/2020
#This the polygon program from last week and converted into a function. 
import turtle
Machuca = turtle.Turtle()

length = int(input ("What is the length for the sides?"))
sides = int(input ("Number of sides in the polygon?"))

Machuca= turtle.Turtle()

#Machuca.color(str(lcolor))
#Machuca.pencolor(str(lcolor))

def drawPolygon(t,sides,length):
    
    for i in range(sides):
    #Machuca.pencolor = (str(lcolor))
    #Machuca.fillcolor = (str(fcolor))
        Machuca.forward(length)
        Machuca.left(360 / sides)

wn = turtle.Screen()
Machuca= turtle.Turtle()
Machuca.speed(5)
wn.bgcolor("lightgreen")
Machuca.pencolor("blue")

mv = -10

for s in range(length, 10*length,40):
   
  drawPolygon(Machuca,sides,s)

  Machuca.penup()
  Machuca.goto(mv,mv)
  Machuca.pendown()
  mv = mv -10
