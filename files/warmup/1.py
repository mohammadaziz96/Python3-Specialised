"""The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num."""

file1=open("travel_plans.txt")
rd=file.read(file1)
num=0
for c in rd:
    num+=1
print(num)
