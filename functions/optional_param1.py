initial=7
def f(x,y=2,z=initial):
    print("x, y, z, are: " + str(x) + ","  + str(y) + ","  + str(z))
f(2)
f(3,z=25) #y remain have default value
f(5,8) # here y value is changed
