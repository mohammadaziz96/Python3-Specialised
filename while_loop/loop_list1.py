"""Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums."""

eve_nums=[]
i=0
while(i<=15):
    if i%2==0:
        eve_nums.append(i)
    i=i+1
print(eve_nums)
