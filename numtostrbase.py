def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]

# num = int(input("Enter number in decimal:"))
# base = int(input("Enter Base:"))
# print(num, "in base", base, "is", toStr(num, base))


class Employee:
    """A Sample employee class"""
    number = 0
    amount = 10000

    def __init__(self, first, last, pay=0):
        self.first = first
        self.last = last
        Employee.number += 1
        self.pay = pay

    def __str__(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay += self.amount

    @classmethod
    def add_num_emp(cls, num):
        cls.number += num

    @classmethod
    def from_string(cls, str):
        first, last = str.split()
        return cls(first, last)


class Developer(Employee):
    amount = 20000

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def rem_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.first, emp.last)

s = "Hodor njbjba"
e1 = Employee.from_string(s)
print(e1)

# emp1 = Employee("Baibhav", "Bista")
# Employee.add_num_emp(5)
# print(Employee.number)

# for num in [1, 2, 3, 4]:
#     print(num + 1)
dev1 = Developer("Baibhav", "Bista", 0, "Python")
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
print(type(e1))

manager1 = Manager("Baibhav", "Bista", 0, [dev1, dev1])
manager1.print_employees()

print(isinstance(manager1, Developer))
print(issubclass(Developer, Employee))
