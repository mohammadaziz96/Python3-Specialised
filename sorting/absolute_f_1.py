l1=[1,2,3,4,5,-1,-5,-9,10]
def absolute(x):
    if x>=0:
        return x
    else:
        return -x
print(sorted(l1, key=absolute))
print(sorted(l1, key=lambda x: absolute(x)))
