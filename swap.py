def main():
	a = int(input("a = "))
	b = int(input("b = "))
	a, b = swap(a, b)
	print("a = {}".format(a))
	print("b = {}".format(b))
#a function can return more than one value	
def swap(a, b):
	return b, a
	
if __name__ == "__main__":
	main()
