"""We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words."""

num_words=0
file1=open("emotion_words.txt")
rd=file.read(file1)
print(rd)
k=rd.split()
for w in k:
    num_words+=1
    print(w)
print(num_words)
