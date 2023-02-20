#Replacing a word in python

def replace_word():
    str = "My name is Kofi and I was born Thursday."
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")

    print(str.replace(word_to_replace, word_replacement))

replace_word()
