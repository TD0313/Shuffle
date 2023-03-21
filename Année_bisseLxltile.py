from random import suffle

chaine_words = input("Insérer une chaine de la forme mot1/mot2/mot3/mot4 :")

words = chaine_words.split("/")

suffle(words)

words_len = len(words)

if words_len < 10:
    print (words[0], words [1])
else:
    print (words[words_len-1],words[words_len-2],words[words_len-3])