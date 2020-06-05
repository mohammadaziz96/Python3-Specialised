x=[1,2,3,4,5,6,7,8,9]
y=[11,22,33,44,55,99,0,12,0]
z=[0,0,1,2,6,9,5,3,2]
#z1=zip(x,y,z)
l1=[]
#print(list(z1))
for i,j,k in zip(x,y,z):
    l1.append(i+j+k)
print(l1)
