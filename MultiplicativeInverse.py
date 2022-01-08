"""
The following program calculates the muliplicative inverse of b mod a. The muliplicative inverse of b mod a is 
denoted b^-1 and is defined as

			b.b^-1 mod a = 1

where b, b^-1 and a are all positive integers.  
"""


import math
import argparse
import sys

def get_arguments():
	# Take in inputs
	parser = argparse.ArgumentParser()
	parser.add_argument("-a", "--a", dest="a", help="The first integer input.")
	parser.add_argument("-b", "--b", dest="b", help="The second integer input.")
	options = parser.parse_args()

	# Validate that the user has specified an input for both variables
	if not options.a:
		print("[-] Please specify an input for a. This algorithm needs two inputs")
		sys.exit(0)
	if not options.b:
		print("[-] Please specify an input for b. This algorithm needs two inputs")
		sys.exit(0)


	# Validate that both inputs are integers. 
	if not options.a.isdigit() or not options.b.isdigit():
		if "." in options.a or "." in options.b: 
			print("[-] This program only accepts intger inputs.")
			sys.exit(0)


	if int(options.a) < 0 or int(options.b) < 0:
		print("[-] Positive Integer expected")
		sys.exit(0)



	return options



def multiplicative_inverse(a,b):
	a0 = a
	b0 = b
	t0 = 0
	t = 1
	q = math.floor(a0/b0)
	r = a0 - (q*b0)

	while(r > 0):
		temp = (t0-(q*t)) % a
		t0 = t
		t = temp
		a0 = b0
		b0 = r
		q = math.floor(a0/b0)
		r = a0 - (q*b0)

	if b0 != 1:
		return None 
	else:
		return t

def main():
	arguments = get_arguments()
	a = int(arguments.a)
	b = int(arguments.b)
	result = multiplicative_inverse(a,b)
	if result is None:
		print(f"[-] {b} has no inverse modulo {a}")
	else:
		print(f"[+] {result} is the inverse of {b} mod {a}")

if __name__ == "__main__":
	main()