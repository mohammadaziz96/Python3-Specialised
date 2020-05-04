file1=open("sample.txt", "r")
three=[]
r=file1.readlines()
for line in r:
    k=line.split()
    three.append(k[2])
    print(line)
print(three)
