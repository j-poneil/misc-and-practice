#Challenge to reverse a string.
#IE. "I Love Code" = "edoC evoL I"

def reverse(str):
	'''reverse(str) takes one string argument when it is called.
	It converts this string into a list of characters,
	reverses the list,
	re-joins the list into a string,
	and finally returns the result to whatever called the function.'''
	string_as_list = list(str)
	string_as_list.reverse()
	return "".join(string_as_list)

print reverse(raw_input("input a string> "))

#To get to the help on cmd line
#from py_firstrevchallenge import reverse
#help(reverse)