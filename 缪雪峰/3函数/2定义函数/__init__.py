def my_abs(x):
    if x>=0:
        return  x
    else:
        return -x

print(my_abs(-50))

def nop():
    pass


def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return  x
    else:
        return -x

import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

print(move(100,100,60,math.pi/6))