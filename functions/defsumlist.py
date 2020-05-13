def accum(lst):
    count=0
    for s in lst:
        count=count+s
    return count
l=[1,2,3,4,5,6,7,8,9]
print(accum(l))
