"""Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well."""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
print(positive_words)

def strip_punctuation(word):
    for pc in punctuation_chars:
        if(pc in word):
            word=word.replace(pc, "")
    return word


def get_pos(word):
    word=strip_punctuation(word)
    listofword=word.split()
    countp=0
    for l_word in listofword:
        if l_word in positive_words:
            print(l_word)
            countp=countp+1
    return countp
