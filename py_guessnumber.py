#computer generates and saves a random number between 0 and user input
#You try to guess the number, program tells you if you are high or low
import random

max_num = int(raw_input("Number guessing game.\nWill generate a random number between\n0 and max_num.\nWhat is the max? >"))

num = random.randint(0,max_num)
guess = max_num + 1
while num != guess:
	guess = int(raw_input("Guess? Between 0 and %d > " % max_num))
	if num > guess:
		print "Higher"
	elif num < guess:
		print "Lower"
	else:
		continue

print "Correct! num: %d == guess: %d" % (num, guess)