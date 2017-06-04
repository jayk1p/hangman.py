import requests
from random import randint

random = (randint(1, 25487))


word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
words = response.content.splitlines()

# print len(words)
# this is to find out how many elements are in your list

selected = words[random]
# print selected
# this is to pick out the random word through the random number

letters = list(selected)
# This separates a word into letters
# print letters

print len(letters), "letters"




a = 0

used = []

while a < 7:
    raw = raw_input("Enter a letter: ")

    if raw in letters:
        print "It's in the word!"
        print [i for i,x in enumerate(letters) if x == raw]
        used.append(raw)
        print "Used letters:", used

    if raw == selected:
        print "That's the word! Nice Job!"
        break

    if raw not in letters:
        print "Incorrect"
        a = a + 1
        print "strike %d" % a
        used.append(raw)
        print "Used letters:", used


print "Thanks for playing!"
