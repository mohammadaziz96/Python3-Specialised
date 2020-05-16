initial=7
def f(x, y=3, z=initial):
    print("x, y, z are: " +str(x)+ "," +str(y)+ "," +str(z))
f(2)
f(2,z=23,y=1)
f(x=20,z=1)
#f(a=10,20,z=1)
#f(z=30, 10, x=1) #keyword argument(z=30) comes always after positional aargument(20)
f(10,z=20,y=2)
#f(20,z=10,x=15)#ggot error because assigned multiple value for x
