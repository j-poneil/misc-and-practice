import math

def FirstFactorial(num):
	"""Accepts non-negative integers. Ex 4! = 24, 8! = 40320"""
	num = math.factorial(num)
	return num

print FirstFactorial(raw_input("Enter a valid non-negative whole number integer > "))

#Originally I had not read about the "math" module. I was initially considering trying some sort of for loop with range(num) and if statements... hmm
