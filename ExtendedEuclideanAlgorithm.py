"""
The following is a an implementation of the Extended Euclidean Algotithm. 
The purpose of this algorithm is find the gcd of two positive integers and to output two intergers s and t such that:

				sa + tb = gcd(a,b) 

The pseudocode for the implementation of the euclidean_algorithm function was sourced from Chapter 6 page 191 (Algorithm 6.2) of 
Cryptography Theory and Practice (4th Edition) by Douglas R. Stinson & Maura B. Paterson.

I added the abiltiy to supply command line arguments to improve usability and also validate the inputs. 

Although I wasn't able to achieve it here it should be possible to also output each of the intermediary steps of the calculation.
"""
import math
import argparse
import sys


# Command Line arguments
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


	return options


# The Extended Euclidean Algorithm itself 
def extended_euclidean_algorithm(a,b):
	a0 = a
	b0 = b
	t0 = 0 
	t = 1
	s0 = 1
	s = 0
	q = math.floor(a0/b0)
	r = a0 - (q*b0)

	while r > 0:
		temp = t0 - (q*t)
		t0 = t
		t = temp
		temp = s0 - (q*s)
		s0 = s
		s = temp
		a0 = b0
		b0 = r
		q = math.floor(a0/b0)
		r = a0 - (q*b0)
    
	r = b0

	return [r,s,t]


def main():
	arguments = get_arguments()
	a = int(arguments.a)
	b = int(arguments.b)
	result = extended_euclidean_algorithm(a,b)
	print(f"[+] gcd({a},{b}) = {result[0]} and \n[+] ({result[1]} x {a}) + ({result[2]} x {b}) = {result[0]}")

if __name__ == '__main__':
	main()
