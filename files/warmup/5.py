"""Using the file school_prompt.txt, assign the third word of every line to a list called three."""

file1=open("school_prompt.txt")
rd=file.readlines(file1)
three=[]
for w in rd:
    w=w.strip().split()
    three.append(w[2])
    print(w)
print(three)
