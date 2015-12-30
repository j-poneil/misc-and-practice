#From http://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
#I kept messing up and eventually just googled proper ways to do it
#Originally I was going to have just one for loop... somehow

def generate_prime_nums(max_num):
	"""Search for and print out prime numbers up to the max number initially given"""
	primes = []
	for num in range(max_num):
		if num > 1:
			prime = True
			for i in range(2,num):
				if (num % i) == 0:
					prime = False
			if prime == True:
				primes.append(num)
	print primes

generate_prime_nums(int(raw_input("Searching for prime numbers.\nWhat is the max number to search up to? > ")))


#Other ways
"""
for num in range(1,101):
    if all(num%i!=0 for i in range(2,num)):
       print num
"""
#other
"""




"""