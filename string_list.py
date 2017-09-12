
def main():
	n = int(input("Enter the number of strings you want: "))
	strings = []
	for i in range(n):
		s = input("Enter string {}: ".format(i+1))
		strings.append(s)
	for j in range(len(strings)):
		for c in strings[j]:
			print(c, end="")
	print()
		
if __name__ == "__main__":
	main()
