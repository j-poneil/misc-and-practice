import math

def FirstFactorial(num):
	"""Accepts non-negative integers. Ex 4! = 24, 8! = 40320"""
	num = math.factorial(num)
	return num

print FirstFactorial(raw_input("Enter a valid non-negative whole number integer > "))

#Originally I had not read about the "math" module. I was initially considering trying some sort of for loop with range(num) and if statements... hmm

def FirstFactorial_m2(num):
	"""Accepts non-negative integers."""
	temp = 1
	while num > 0:
		temp = temp * num
		num = num - 1
	return temp

#This works... but not quick and easy to think through... better way is what?

#temp = 1
#while num > 0:
#	temp = temp * num
#	num = num - 1
#return temp

#temp = 1
#num = 3
#..temp = 1 * 3 == 3
#..num = 3 - 1 == 2

#..temp = 3 * 2 == 6
#..num = 2 - 1 = 1

#..temp = 6 * 1 = 6
#..num = 1 - 1 = 0

#num !> 0
#thus return temp, temp = 6


def smartfactorial(num):
	if num == 0:
		return 1 #This contingency is ONLY for if/when the input number is 0. It will get to be equal to zero eventually if the input was a valid number.
	else:
		return num * smartfactorial(num - 1) #Brilliant. By calling the function inside itself, it piles up num * (num-1) * (num-2) * etc... to multiply at the end and return the full factorial.

#Smarter way to do it IMO.