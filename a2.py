string = []
empty_string = ("")
word = ("")
def sort_word(word):
    string = list(word)
    string.sort(key=lambda x: x.lower())
    empty_string = "".join(string)
    return empty_string
print(sort_word(word))