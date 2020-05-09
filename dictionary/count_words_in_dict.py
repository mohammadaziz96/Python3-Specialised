#sentance= "The dog chosed the rabbit into the forest but the rabbit was too quick."
file1=open("sample.txt", "r")
f=file1.read()
words=f.split()
w={}
for word in words:
    if word not in w:
        w[word]=0
    w[word]=w[word]+1
print(w)
