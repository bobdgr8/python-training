def fibo(n):
	a, b = 0, 1
	while a < n:
		print(a, end = " ")
		a, b = b, a + b
	
def main():
	n = int(input("Upto: "))
	fibo(n)
	print()
	
	
if __name__ == "__main__":
	main()
