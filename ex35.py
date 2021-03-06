#This function defines break words function which will perform the split function and return words string
def break_words(stuff):
	'''This function will break up words for us.'''
	words = stuff.split(' ')
	return words

#this function sorts words
def sort_words(words):
	'''Sorts the words.'''
	return sorted(words)

#pops off words
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(1)
    print word

#pop off last words
def print_last_word(words):
	'''Prints the first word after popping it off.'''
	word = words.pop(-1)
	print word


def sort_sentence(sentence):
	'''Takes in a full sentence and returns the sorted.'''
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	'''Prints the first and last words of the sentence.'''
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)


def print_first_and_last_sorted(sentence):
	'''Sorts the words then prints the first and last one.'''
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
