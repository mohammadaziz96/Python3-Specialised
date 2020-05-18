#Print Alphabets that how many times each appeared in sorted order.

l=["E","F","B","A","D","I","I","C","B","A","D","D","E","C"]
ld={}
for x in l:
    if x not in ld:
        ld[x]=0
    ld[x]=ld[x]+1
#print(ld)
for x in sorted(ld.keys()):
    print("{} appears {} times".format(x, ld[x]))
