"""Write code that sum up a list containing numbers, but instead uses a while loop. Assign the accumulator variable to the name accum."""
list1 = [8, 3, 4, 5, 6, 7, 9]
accum=0
ele=0
while(ele<len(list1)):
    accum=accum+list1[ele]
    ele+=1
print(accum)
