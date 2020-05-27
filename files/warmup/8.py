"""Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words."""

p_words=[]
file1=open("school_prompt.txt")
rd=file.read(file1).strip().split()
for c in rd:
    if "p" in c:
        p_words.append(c)
print(p_words)
