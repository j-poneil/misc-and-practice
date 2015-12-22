import string

#remember chr() and ord()
#valid between 32-126
#A-Z is 65-90
#a-z is 97-122


def LetterChanges(str):
	str_len = len(str)
	shift = 1
	for i in range(str_len):
		#print str[i]
		if 65 <= str[i] < 89:
			print chr(ord(str[i]) + 1)
		elif str[i] == 90:
			print chr(ord(str[i]) - 26)
		elif 97 <= str[i] < 121:
			print chr(ord(str[i]) + 1)
		elif str[i] == 122:
			print chr(ord(str[i]) - 26)
		else: #should I have it do the same thing with non-letters?
			print chr(ord(str[i]) + 1) #print str[i]
	
	#That print without starting a new line thing would be useful right about now


print LetterChanges(raw_input("enter a string > "))