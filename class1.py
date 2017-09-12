from student import Student
import csv

students = []

for i in range(3):
	print("Student " + str(i+1))
	name = input("Name: ")
	dorm = input("Dorm: ")
	students.append(Student(name, dorm))

file = open("students.csv", "w")
writer = csv.writer(file)
for stud in students:
	writer.writerow((stud.name, stud.dorm))
	
file.close()


