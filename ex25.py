# -*-  coding: utf-8 -*-
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after poping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after poping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentences):
	"""Take in a full sentence and returns the sorted words."""
	words = break_words(sentences)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentences)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentences)
	print_first_word(words)
	print_last_word(words)
