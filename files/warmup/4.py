"""Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars."""

file1=open("school_prompt.txt")
rd=file.read(file1)
beginning_chars=rd[:30]
print(beginning_chars)

