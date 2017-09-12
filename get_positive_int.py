
def main():
	i = get_positive_int();
	print(i)
	
def get_positive_int():
	while True:
		n = int(input())
		if(n > 0):
			break
	return n
	
if __name__ == "__main__":
	main()
	
