height = int(input("Height: "))

for j in range(1, height+1):
	for i in range(height-j):
		print(" ", end = "")
	for i in range(j):
		print("#", end = "")
	print("  ", end = "")
	for i in range(j):
		print("#", end = "")
	print()
	
