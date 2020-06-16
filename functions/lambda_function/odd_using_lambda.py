import numpy as np
A=np.array([1,45,50,34,12,35,77,80,11,51,61,10,20,40,66])
#print(A)
k=list(filter(lambda x: (x%2 != 0), A))#filter only returns true value (filter takes two argument one is function and other is list or any iterale object)
print(type(A))
print("Number of a list {}".format(A))
print("odd numbers are {}".format(k))
