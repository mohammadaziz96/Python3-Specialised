l1=[1,4,7,-5,6,10]
l2=["Cherry", "Apple", "Blueberry"]
l1.sort()
print(l1) #changes reflects in original list as well
l2.sort()
print(l2)#changes reflected in original list
s1=["hey", "I", "am", "aziz"]
s2=[1,5,0,1,3,5,6,-1,-5,-7]
s3=sorted(s1) # original list remains unchanged
print(s3)
print(s1)
s4=sorted(s2) # Original list remains unchanged
print(s4)
print(s2)
print(s2.sort()) #returns value is None
