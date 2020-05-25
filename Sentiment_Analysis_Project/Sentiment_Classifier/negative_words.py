"""Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well."""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for pc in punctuation_chars:
        if(pc in word):
            word=word.replace(pc, "")
    return word

def get_neg(word):
    word=strip_punctuation(word)
    listofword=word.split()
    countn=0
    for n_word in listofword:
        if n_word in negative_words:
            countn=countn+1
    return countn



