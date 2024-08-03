#first we import the libary
import turtle

#define some colors
colors = ['red','yellow','green','purple','blue','orange']

#set up the turtle and set the background color
t = turtle.Pen()
turtle.bgcolor('black')

#now to the movements
for x in range(200): #you can choose the number of iterations
    #set the color
    t.pencolor(colors[x%6])
    
    #set the width
    t.width(x/100+1)
    
    #move the turtle
    t.forward(x)
    
    #rotate the turtle
    t.left(59)

