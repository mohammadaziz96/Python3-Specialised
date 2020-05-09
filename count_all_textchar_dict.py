file1=open("sample.txt", "r")
f=file1.read()
x={}
for c in f:
    if c not in x:
        x[c]=0
    x[c]=x[c]+1
print(x)
