"""Create a list called emotions that contains the first word of every line in emotion_words.txt."""

file1=open("emotion_words.txt")
rd=file.readlines(file1)
emotions=[]
for w in rd:
    w=w.strip().split()
    emotions.append(w[0])
    print(w)
print(emotions)
