"""Assign to the variable num_lines the number of lines in the file school_prompt.txt."""

file1=open("school_prompt.txt")
rd=file.readlines(file1)
num_lines=0
for n in rd:
    n=n.strip()
    num_lines+=1
    print(n)
print("number of lines in the file are {}".format(num_lines))

