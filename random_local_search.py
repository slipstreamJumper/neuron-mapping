import sys
from math import *
import random

def forwardMultiplyGate(x, y): 
    return x*y

x = -2
y = 3

tweak_amount = 0.01
best_x = x
best_y = y
best = float('-inf')

for i in range(100):
    trial_x = x + tweak_amount * ((random.random() * 2) - 1)
    trial_y = y + tweak_amount * ((random.random() * 2) - 1)
    out = forwardMultiplyGate(trial_x, trial_y)
    #print("Trial X: " + str(trial_x) + " Trial Y: " + str(trial_y))
    #print("Out: " + str(out))
    if out > best:
        best_x = trial_x
        best_y = trial_y
        best = out


print("Best x: " + str(best_x))
print("Best y: " + str(best_y))
print("Best output: " + str(best))
