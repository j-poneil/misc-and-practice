import string

def LongestWord(sentence):
	print sentence #pre-cleaning
	sentence = sentence.translate(None, string.punctuation)
	print sentence #post-punctuation cleaning
	sentence = sentence.translate(None, string.digits)
	print sentence #post-digit cleaning
	sentence = sentence.split(" ")
	print sentence #post-split into strings in a list
	num_words = len(sentence)
	print num_words #count of number of words/items/elements in list "sentence"
	print "----------------------------------"
	
	for i in range(num_words):
		print len(sentence[i]) #Prints the length of each word from index 0 to index "num_words - 1"
	
	print "----------------------------------"
	
	for i in range(num_words):
		print len(sentence[i]) #Prints the length of each word from index 0 to index "num_words - 1"
	#	x = 0
	#	if len(sentence[i]) > x:
	#			x = len(sentence[i])
	#	
	#	print sentence[x - 1]

	print max(sentence, key=len) #seems like cheating. I need to think more about how I was trying to do it above with commented out code
	
	return sentence


print LongestWord(raw_input("Input a string, add punctuation for better test. > "))