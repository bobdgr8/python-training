from stud import Student

students = []
for i in range(3):
	print("Student {}".format(i+1))
	name = input("Name: ")
	dorm = input("Dorm: ")
	students.append(Student(name, dorm))
	
print(students)
for student in students:
	print("{} is in {}".format(student.name, student.dorm))
	
