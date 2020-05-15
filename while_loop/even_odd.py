x=0
while x<10:
    if x%2==0:
        x+=3
        continue
    if x%3==0:
        x+=5
    x+=1
print("X has the value:" +str(x))
