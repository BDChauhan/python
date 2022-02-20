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

# >>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.