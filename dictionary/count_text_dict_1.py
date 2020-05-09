file1=open("sample.txt", "r")
f=file1.read()
d={}
d["t"]=0
d["s"]=0
for c in f:
    if c=="t":
        d["t"]=d["t"]+1
    else:
        d["s"]=d["s"]+1
print("Number of t in file is:" +str(d["t"]) + " times occur")
print("Number of s in file is:" +str(d["s"]) + " times occur")

