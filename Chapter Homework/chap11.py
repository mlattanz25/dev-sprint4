#Homework - Chapter 11

#11.9

def print_hist(duplicates):
    
	for c in duplicates:
		print c, duplicates[c]

duplicates = dict()
print duplicates
{}
if 
return true





#Solutions:

def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print has_duplicates(t)
    t.append(1)
    print has_duplicates(t)

    t = [1, 2, 3]
    print has_duplicates2(t)
    t.append(1)
    print has_duplicates2(t)










#11. Function needs to read wordlist and find rotate pairs

def rotate_word ():
	print_hist(w):
    for a in w:
		print a, w[a]
w = wordlist ('dogs')
print_hist(w)

for wordlist (w)









#Solutions:

from pronounce import read_dictionary
phonetic = read_dictionary()

def make_word_list():
    """read the words in words.txt and return a dictionary
    that contains the words as keys"""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d

wordlist = make_word_list()

def homophones(a, b):
    """return True if words (a) and (b) can be pronounced the
    same way, False otherwise.

    If either word is not in the pronouncing dictionary, return False
    """
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]

def check_word(word):
    """check to see if the word has the following property:
    removing the first letter yields a word in (d),
    and removing the second letter yields a word in (d)."""
    word1 = word[1:] 
    if word1 not in wordlist: return False
    if not homophones(word, word1): return False

    word2 = word[0] + word[2:]
    if word2 not in wordlist: return False
    if not homophones(word, word2): return False

    return True

def check_all_words():
    for word in wordlist:
        if check_word(word):
            print word

check_all_words()



