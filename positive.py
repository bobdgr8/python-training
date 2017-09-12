def main():
	n = int(get_positive())
	print("{} is a positive integer".format(n))

def get_positive():
	i = 0
	while i <= 0:
		i = float(input("N is "))//1
	return i

main()
