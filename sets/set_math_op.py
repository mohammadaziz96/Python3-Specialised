A={1,2,"Aziz",7,8,6}
B={2,8,"Hamza","Sara"}
C=A&B # & takes intersection of both sets A and B and assigh into C
print("Intersection is: {}".format(C))
D=A.union(B) # Union method takes union of both sets
print("Union is : {}".format(D))
E={1,2,3,4,5,6,7,8,9}
F={1,2,3}
print(F.issubset(E))
print(E.issubset(F))
A1=[20,30,40]
for i in A1:
    A.add(i)
print(A)
k=2
print(A.remove("Aziz"))

