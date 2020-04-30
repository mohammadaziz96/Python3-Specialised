#print each 3 line from text file.
file1=open("sample.txt", "r")
#r=file1.read()#not in list
r=file1.readlines()# read as list
for lin in r[:3]:
    lin=lin.rstrip()
    print(lin)
file1.close()

