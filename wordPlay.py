# breaking of words from sentence
def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def firstLast(words):
    word = words.pop(0)
    print(word)
    word = words.pop(-1)
    print(word)




import sys, time 
 
for char in "hello, world.": 
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.2) 

