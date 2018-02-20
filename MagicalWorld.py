def check_prime(i):
	divisor = 2 # we start checking by dividing by 2
	count = 2 # This represents 1 and the number itself, which are not included when checking primality
	while i != divisor:
		if i % divisor == 0:
			count += 1
		else:
			pass
		divisor += 1
	if count == 2:
		return True
 
def nearest_lower_prime(i):
	lower = i - 1
	result = check_prime(lower)
	while result != True:
		lower -= 1
		result = check_prime(lower)
	return lower
 
def nearest_upper_prime(i):
	upper = i + 1
	result = check_prime(upper)
	while check_prime(upper) != True:
		upper += 1
		result = check_prime(upper)
	return upper
 
 
if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		N = int(input())
		S = raw_input()
		dhanajay_list = []
		for char in S:
			n = ord(char)
			lower_ascii = nearest_lower_prime(n)
			upper_ascii = nearest_upper_prime(n)
			if check_prime(n) == True:
				dhanajay_list.append(char)
			elif n < 65:
			    while not chr(upper_ascii).isalpha():
			        upper_ascii = nearest_upper_prime(n)
			        n += 1
			    dhanajay_list.append(chr(upper_ascii))
			elif n > 122:
			    while not chr(lower_ascii).isalpha():
			        lower_ascii = nearest_lower_prime(n)
			        n -= 1
			    dhanajay_list.append(chr(lower_ascii))
			else:
				if chr(lower_ascii).isalpha() and (abs(n - lower_ascii) == abs(n - upper_ascii) \
				or abs(n - lower_ascii) < abs(n -upper_ascii)):
					dhanajay_list.append(chr(lower_ascii))
				elif chr(upper_ascii).isalpha():
					dhanajay_list.append(chr(upper_ascii))
				else:
				    dhanajay_list.append(chr(lower_ascii))
		print("".join(dhanajay_list))