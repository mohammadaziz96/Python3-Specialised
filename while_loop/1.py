#Take 10 integers from keyboard using loop and print their average value on the screen.
t=0
a=10
while a>0:
    n=int(input("Enter number:"))
    t=t+n
    a-=1
print("The average of numbers are {}".format(t/10))

