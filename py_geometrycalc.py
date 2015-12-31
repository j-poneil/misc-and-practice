#Can calculate some areas and volumes of simple shapes

import math #for math.pi

print "What shape would you like to calculate the area or volume of?"
print '2D:\n\tTriangle=\t\t\t"tri"\n\tSquare/Rectangle/Parallelogram=\t"rect"\n\tTrapezoid=\t\t\t"trap"\n\tCircle=\t\t\t\t"cir"'
print '3D:\n\tCube=\t\t\t\t"cube"\n\tRectangular Prism=\t\t"rectp"\n\tCylinder=\t\t\t"cyl"\n\tSphere=\t\t\t\t"sph"'
print 'Numbers entered can be floating point'
print "-"*30

def area_tri(a,b):
	return (0.5 * a) * b

def area_rect(a,b):
	return a * b

def area_trap(a,b,c):
	return (0.5 * (a + b)) * c

def area_cir(a):
	return math.pi * (a ** 2)



def volume_cube(a):
	return (a ** 3)

def volume_rectp(a,b,c):
	return a * b * c

def volume_cyl(a,b):
	return math.pi * (a ** 2) * b

def volume_sph(a):
	return float(4/3) * math.pi * (a ** 3)



def split_and_assign(input_string):
	"""Splits a string into a list, then list items into individual variables. Takes up to 3 variables."""
	#Could probably make a chunk of code more elegant than this that could return any number of variables
	#Without first having to write them out and test for each one in this clunky way
	#Maybe iterating through loop(s)
	#Hmm...
	input_list = input_string.split(" ")
	number_of_inputs = len(input_list)
	
	if number_of_inputs > 3:
		print "Error, more than 3 inputs detected"
	elif number_of_inputs == 3:
		a,b,c = float(input_list[0]),float(input_list[1]),float(input_list[2])
		return a,b,c
	elif number_of_inputs == 2:
		a,b = float(input_list[0]),float(input_list[1])
		return a,b
	elif number_of_inputs == 1:
		a = float(input_list[0])
		return a
	else:
		print "Error. Invalid input."
	
	
	

user_input = raw_input("Input? > ")
print "-"*30

if user_input == "tri":
	tri_string = raw_input("Input base and height, with a space between them. IE '10 50' >")
	a,b = split_and_assign(tri_string)
	print area_tri(a,b)
elif user_input == "rect":
	rect_string = raw_input("Input width and height, with a space between them. IE '5 4' >")
	a,b = split_and_assign(rect_string)
	print area_rect(a,b)
elif user_input == "trap":
	trap_string = raw_input("Input the length of the parallel sides first, then height. IE '5 8 2' >")
	a,b,c = split_and_assign(trap_string)
	print area_trap(a,b,c)
elif user_input == "cir":
	cir_string = raw_input("Input radius of the circule. IE '5' >")
	a = split_and_assign(cir_string)
	print area_cir(a)
elif user_input == "cube":
	cube_string = raw_input("Input the length of one side. IE '2' >")
	a = split_and_assign(cube_string)
	print volume_cube(a)
elif user_input == "rectp":
	rectp_string = raw_input("Input the length, width, and height. IE '2 3 4' >")
	a,b,c = split_and_assign(rectp_string)
	print volume_rectp(a,b,c)
elif user_input == "cyl":
	cyl_string = raw_input("Input the radius and height. IE '5 20' >")
	a,b = split_and_assign(cyl_string)
	print volume_cyl(a,b)
elif user_input == "sph":
	sph_string = raw_input("Input the radius from the center of the sphere. IE '10' >")
	a = split_and_assign(sph_string)
	print volume_sph(a)
elif user_input == None:
	print "Error"
else:
	print "Error"








