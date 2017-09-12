def main():
	num_as_string = input("Number: ")
	if not valid_or_not(num_as_string):
		print("INVALID")
		exit(1)
	else:
		company_detector(num_as_string)
	
def validornot(s):

	total = 0
	totalodd, totaleven = 0, 0
	for i in range(0, len(s), 2):
		totalodd += int(s[i])
	for i in range(1, len(s), 2):
		totaleven += int(s[i])

	if (len(s)-1)%2 == 0:
		totaleven *= 2
	else:
		totalodd *= 2

	total = totaleven + totalodd
	if total % 10 == 0:
		return True
	else:
		return False

def company_detector(s):
	if len(s) == 15 and (s[:2] == "34" or s[:2] == "37"):
		print("AMEX")
	elif (len(s) == 13 or len(s) == 16) and s[0] == "4":
		print("VISA")
	elif (len(s) == 16) and s[:2] in {"51", "52", "53", "54", "55"}:
		print("MASTERCARD")
	else:
		print("INVALID")
