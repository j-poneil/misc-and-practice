#Sentence randomizer
#Input a sentence, the longer the better.
#It is broken up into words in a list, list entries are randomized
#randomization is via:
#pop a random string out of the first list and append it to the new list, repeat until no entries
#Then it is re-printed as a string, finally.
#This was pretty easy to do. Probably not the most efficient way, but I think it works pretty well.
#Didn't take too long to think up how to do it.
import string
import random

def randomizer(original):
	original_as_list = original.split(" ")
	scrambled_list = []
	while len(original_as_list) != 0:
		scrambled_list.append(original_as_list.pop(random.randint(0,len(original_as_list) - 1)))
	scrambled_sentence = " ".join(scrambled_list)
	return scrambled_sentence


sentence = raw_input("Input a long sentence with interesting words >")

rand_sentence = randomizer(sentence)
rand_sentence2 = randomizer(sentence)
rand_sentence3 = randomizer(sentence)

print "Original > %s" % sentence
print "-"*30
print "Rand1 > %s" % rand_sentence
print "Rand2 > %s" % rand_sentence2
print "Rand3 > %s" % rand_sentence3