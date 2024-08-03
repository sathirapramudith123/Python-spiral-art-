from turtle import *
import random

setup(1000,1000)


def tiling(x,y,s,l):

    #we have reached the final level of recursion and we draw
    
    if l == 0:

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
    #split the screen and goto next level of recursion
    else:
        s/=2
        l -=1
        tiling(x-s,y+s,s,l)
        tiling(x+s,y+s,s,l)
        tiling(x-s,y-s,s,l)
        tiling(x+s,y-s,s,l)


tiling(0,0,400,1)        
exitonclick()
