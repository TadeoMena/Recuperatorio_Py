import random

def listfiller():
    words = ["Natural","Entero","Racional","Real","Imaginario"]
    rwords = []
    for w in range(20):
        index = random.randint(0,4)
        rwords.append(words[index])
    return rwords

def uniquefilter():
    unique = []
    for w in listfiller():
        if w not in unique:
            unique.append(w)
    return unique

def dictmaker():
    d = {}
    for w in unique_words:
        d[w] = 0
    countdict = wordcounter(d)
    return countdict

def wordcounter(dict):
    for w in wordlist:
        if w in dict:
            dict[w] += 1
    return dict

wordlist = listfiller()
unique_words = uniquefilter()
dictionary = dictmaker()
print(dictionary)