import math

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

if __name__ == '__main__':
	a = 4534563456
	b = 4875678564
	result = extended_euclidean_algorithm(a,b)
	print(f"[+] gcd({a},{b}) = {result[0]} and \n[+] ({result[1]} x {a}) + ({result[2]} x {b}) = {result[0]}")
