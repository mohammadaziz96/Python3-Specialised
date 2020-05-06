file1=open("sample.txt","r")
f=file1.read()
count=0
for c in f:
    if c=="t":
        count=count+1
print("t: " + str(count) + " occurrences")
