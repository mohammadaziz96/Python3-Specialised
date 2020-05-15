def begining(l):
    lst=[]
    i=0
    while(i<10):
        if(l[i]=="bye"):
            break
        lst.append(l[i])
        i+=1
    return lst
l=["he","is","man","of","power","bye","she","want","to","marry","with","him","bye"]
print(begining(l))
