import numpy as np
from functools import reduce
A=np.array([1,2,3,4,5,6,7,7,19])
sum=reduce(lambda x,y: x+y, A) #x is current value and y is previous stored result
#x=1,y=2 x+y=3
#x=3,y=3 x+y=6
#x=4,y=6 x+y=10
#and so on
#once it reaches at the last peace of data reduce will return the final value
#reduce function returns a list
print(sum)
