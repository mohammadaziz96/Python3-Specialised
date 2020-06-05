a=["a","b","c","d","e","f","g","h"]
for i in enumerate(a): #bydefault enumerate index starts from 0
    print(i)
for j in enumerate(a,100): # index starts from 100
    print(j)
for k,l in enumerate(a,101):
    print(k,l)
