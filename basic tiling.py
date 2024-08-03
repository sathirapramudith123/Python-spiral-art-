from turtle import *
import random

setup(1000,1000)


def tiling(x, y,s, l, mode="straight"):

    #we have reached the final level of recursion and we draw
    
    if l == 0:


        if mode == "straight":
                #vertical line
                if random.random() <0.5:            
                    penup()
                    goto(x,y-s)
                    pendown()
                    goto(x,y+s)

                    
                #horizonatl line
                else:
                    penup()
                    goto(x-s,y)
                    pendown()
                    goto(x+s,y)
                
        elif mode == "diagonal":
                 #top left to bottom line
                if random.random() <0.5:            
                    penup()
                    goto(x-s,y+s)
                    pendown()
                    goto(x+s,y-s)

                    
                #bottom left to top line
                else:
                    penup()
                    goto(x-s,y-s)
                    pendown()
                    goto(x+s,y+s)
             
    #split the screen and goto next level of recursion
    else:
        s/=2
        l -=1
        tiling(x-s,y+s,s,l,mode)
        tiling(x+s,y+s,s,l,mode)
        tiling(x-s,y-s,s,l,mode)
        tiling(x+s,y-s,s,l,mode)

width(2)
hideturtle()
tracer(False)
tiling(0,0,400,5,mode = "diagonal")
tracer(True)
exitonclick()
