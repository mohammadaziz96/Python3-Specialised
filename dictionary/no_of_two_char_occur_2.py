file1=open("sample.txt", "r")
f=file1.read()
t_count=0
s_count=0
for c in f:
    if c=="t":
        t_count= t_count+1
    elif c=="s":
        s_count = s_count+1
print("t: " + str(t_count) + " Occurences")
print("s: " + str(s_count) + " Occurences")
