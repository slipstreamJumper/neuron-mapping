# Partial Derivative Calculator
# dx/dz (x,y) = f(x+h,y) - f(x,y) / h
# h = very small tweak amount ~ 0.0001 

import sys
from math import *
import random


# equation matches the function f = x^2y
#dz/dx= 2xy
#dz/dy = x^2

def partialDir(x,y, h):
    fx = lambda x,y: (x**2)*y     
    dzdx = lambda x,y: 2*x*y
    dzdy = lambda x,y: x**2    
    print("fx: " + str(fx(3,2)))
    print("dzdx: " + str(dzdx(3,2)))
    print("dzdx + h: " + str(dzdx(3+h,2)))
    print("dzdy: " + str(dzdy(3,2)))
    print("dzdy + h: " + str(dzdy(3+h,2)))
    
    
#    xph = (x+h**2)*y
#    print("(x+h**2)*y " + " :: " + str(xph))
#    xph = xph / h
#    print("xph / h " + " :: " + str(xph))
#    yph = (x**2)*(y+h)
#    print("(x**2)*(y+h) " + " :: " + str(yph))
#    yph = yph / h
#    print("yph / h " + " :: " + str(yph))
#    
#    print("xph: " + str(xph))
#    print("yph: " + str(yph))

        
   
def forwardMultiplyGate(x, y): 
    return x*y
    

def getPartials(inputList, hVal):
    returnVector = []
    
    for i in inputList:    
        x = i[0]
        y = i[1]
        
        h = hVal
                
        out = forwardMultiplyGate(x,y)
        #print("f(x,y): " + str(out))
        
        # compute derivative with respect to x
        # f(x+h, y) - f(x,y) / h
        xph = x + h
        dx = forwardMultiplyGate(xph, y)
        #print("f(x + h, y): " + str(dx))
        dir_x = (dx-out)/h
        print("f(x+h,y) - f(x,y) / h: " + str(dir_x))
        
        # compute derivative with respect to y
        # f(x, y+h) - f(x,y) / h
        yph = y + h
        dy = forwardMultiplyGate(x, yph)
        #print("f(x, y + h): " + str(dy))
        dir_y = (dy-out)/h
        print("f(x,y+h) - f(x,y) / h: " + str(dir_y))
        
        returnVector.append([dir_x, dir_y])
    return returnVector
#step_size = 0.01
#new_x = x + step_size * dir_x
#new_y = y + step_size * dir_y
        
#new_out = forwardMultiplyGate(new_x, new_y)
#print("New Out: " + str(new_out))

