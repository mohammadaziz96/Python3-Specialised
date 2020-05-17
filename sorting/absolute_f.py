# make a function to find absolute values.

l=[1,7,4,-2,3]
l1=[]
def absolute(x): # -x becomes x like in maths |-x|=x
    if x>=0:
        return x
    else:
        return -x
#print(absolute(3))
#print(absolute(-119))
for y in l:
    a=absolute(y)
    print(a)
    l1.append(a)
print("Absolute value of {} is {}: " .format(l, l1))
l2=sorted(l, key=absolute) #sort using absolute using key function
#key function takes each item from list l1 and pass to absolute and make it absolute.
print(l2)
print(sorted(l1, key=absolute))
