import math

def main():
	primes = []
	count = 0
	i = 1
	while count <= 1000:
		if isPrime(i):
			primes.append(i)
			count = count + 1
		i = i + 1

	print(primes)



def isPrime(n):
	for x in range(2, n):
		if n % x == 0:
			return False
	return True


if __name__ == "__main__":
	main()