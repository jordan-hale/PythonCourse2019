import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int

## make all characters capitalized
def shout(txt):
	return txt.upper()

## reverse all characters in string
def reverse(txt):
	temp = [i for i in txt]
	return "".join(temp[::-1])

## reverse word order in string
def reversewords(txt):
	return txt.split()[::-1]

## reverses letters in each word
def reversewordletters(txt):
	return [reverse(i) for i in txt.split()]

## change text to piglatin.. google it!
def piglatin(txt):
	txt.split()
	while i for i in txt not in ['A', 'E', 'I', 'O', 'U',  'Y', 'a', 'e', 'i', 'o', 'u', 'y']
		continue
		if i for i in txt in ['A', 'E', 'I', 'O', 'U',  'Y', 'a', 'e', 'i', 'o', 'u', 'y']
			break


## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.

string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]
