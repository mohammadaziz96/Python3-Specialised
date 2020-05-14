def stop_at_four(l):
    lst=[]
    count=0
    while(l[count]!=4):
        lst.append(l[count])
        count=count+1
    return lst
k=[1,2,6,7,8,9,2,6,2,4,33,]
print(stop_at_four(k))
