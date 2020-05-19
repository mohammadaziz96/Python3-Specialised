punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    for r in punctuation_chars:
        if r in word:
            word=word.replace(r,"")
    return word
print(strip_punctuation("asdfg@wer"))




