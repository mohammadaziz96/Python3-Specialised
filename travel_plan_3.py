#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

file_12=open("travel_plan.txt", "r")
r=file_12.read()
first_chars=r[0:33]
print(first_chars)
