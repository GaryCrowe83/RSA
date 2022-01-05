"""
The following is a an implementation of the Euclidean Algotithm. 
The purpose of this algorithm is find the gcd of two positive integers. 

The pseudocode for the implementation of the euclidean_algorithm function was sourced from Chapter 6 page 189 (Algorithm 6.1) of 
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

# The euclidean algorithm itself 
def euclidean_algorithm(a,b):
	remainders = []
	q = []
	remainders.append(a)
	remainders.append(b)
	m = 1

	while remainders[m] != 0:
		current_q = math.floor(remainders[m-1]/remainders[m])
		q.append(current_q)
		next_remainder = remainders[m-1] - (current_q*remainders[m])
		remainders.append(next_remainder)
		m = m + 1
    
	m = m - 1

	return [q, remainders[m]]


def main():
	arguments = get_arguments()
	result = euclidean_algorithm(int(arguments.a), int(arguments.b))
	gcd = result[1]

	print(f'[+] gcd({arguments.a}, {arguments.b}) = {gcd}')


if __name__ == "__main__":
	main()