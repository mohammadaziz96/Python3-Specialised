file_1=open("sample.txt", "r")
r=file_1.read()
count=0
for i in r:
    i=i.strip()
    count=count+1
num=count
print(count)
