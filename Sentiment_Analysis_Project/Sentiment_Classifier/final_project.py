punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(word):
    word=strip_punctuation(word)
    listofword=word.split()
    countn=0
    for n_word in listofword:
        if n_word in negative_words:
            countn=countn+1
    return countn

def get_pos(word):
    word=strip_punctuation(word)
    word=word.strip()
    listofword=word.split()
    countp=0
    for l_word in listofword:
        if l_word in positive_words:
            print(l_word)
            countp=countp+1
    return countp
def strip_punctuation(word):
    for pc in punctuation_chars:
        if(pc in word):
            word=word.replace(pc, "")
    return word

def WriteInFile(resulting_data):
    resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    
    file3=open("resulting_data.csv")
    r2=file3.readlines()
    for j1 in r2:
        print(j1)

    file2=open("project_twitter_data.csv")
    r=file2.readlines()
    for i in r:
        j=i.strip().split(",")
        resulting_data.write("{}, {}, {}, {}, {}".format(j[1], j[2], get_pos(j[0]), get_neg(j[0]), get_pos(j[0])-get_neg(j[0])))
        resulting_data.write("\n")

file1=open("resulting_data.csv", "w")
WriteInFile(file1)
