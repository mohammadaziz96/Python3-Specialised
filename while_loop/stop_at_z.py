def stop_at_z(l):
    lst=[]
    t=True
    i=0
    while(t):
        if(l[i]=="z"):
            break
        lst.append(l[i])
        i+=1    
    return lst
l=["a","b","c","d","z"]
print(stop_at_z(l))
