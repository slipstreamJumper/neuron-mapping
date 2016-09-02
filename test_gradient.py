import math 
import partial_derivative as pd

inputList = [[-2,3], [-3,5], [-4,6]]
outputList = pd.getPartials(inputList, .0001)

#x_gradient = reduce(lambda x, y: x+y, [float(a[0]) for a in outputList])
x_gradient = [float(a[0]) for a in outputList]
#y_gradient = reduce(lambda x, y: x+y, [float(a[1]) for a in outputList])
y_gradient = [float(a[1]) for a in outputList]

print(x_gradient)
print(y_gradient)

print [pd.forwardMultiplyGate(a[0], a[1]) for a in outputList]


pd.partialDir(3,2,.001)



#a = map(lambda x: x+1)