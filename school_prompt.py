# Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

file_4=open("sample.txt", "r")
r=file_4.read().split()
p_words=[]
for i in r:
    if "p" in i:
        p_words.append(i)
print(p_words)
