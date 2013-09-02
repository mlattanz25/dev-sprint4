#10.7

def is_anagram ():
anagram = ['dogs', 'gods']
for i in range (len(anagram)):
	t.sort()
	if 
	return True

#Solution:

def is_anagram(t,u):
    if sorted(t)== sorted (u):
        return True
    else:
        return False
print is_anagram('realtor', 'rotlear') # True
print is_anagram('superpuff','local') # False
print is_anagram('alla', 'lala') # True
print is_anagram('tools', 'stool') # True
print is_anagram('double', 'trouble') # False








#10.13

	interlocking words ["shoe", "cold"]
def interlock ():
	shoe = [0, 1, 2, 3]
	cold = [0, 1, 2, 3]

	

#Solution 
	
def interlock(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 