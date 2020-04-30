file1=open("sample.txt", "r")
#r=file1.read()#not in list
r=file1.readlines()# read as list
print(r[:3])
file1.close()
