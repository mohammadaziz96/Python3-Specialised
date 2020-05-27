"""Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars."""

file1=open("travel_plans.txt")
rd=file.read(file1)
first_chars=rd[:33]
print(first_chars)
