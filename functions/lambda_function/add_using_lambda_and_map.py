import numpy as np
A=np.array([1,2,3,4,5,6,7,8,9,10])
B=np.array([2,3,4,5,6,7,8,9,10,11])
multby2=list(map(lambda x: x*2, A))
add=map(lambda x, y: x+y, A,B) #map function uses argument as
#function and iterable object like list. map function returns
#an map object.map function passes each element from iterable to the function.
print(multby2)
print(list(add))
