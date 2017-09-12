import csv
from stud import Student

students = []
for i in range(3):
	print("Student {}".format(i+1))
	name = input("Name: ")
	dorm = input("Dorm: ")
	students.append(Student(name, dorm))
	
file = open("students.csv", "w")
writer = csv.writer(file)
for student in students:
	writer.writerow((student.name, student.dorm))
file.close()

