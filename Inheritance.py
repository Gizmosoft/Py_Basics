class Employee(object):
    raise_amount = 1.02
    def __init__(self, first, last, pay, status):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@gizmosoft.com'
        self.status = status

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def all(self):
        return '{} {} {} {} {}'.format(self.first, self.last, self.pay, self.email, self.status)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, status, prog_lang):
        super().__init__(first, last, pay, status)  #Employee().__init__(self, first, last, pay) -->This is used for Multiple Inheritance
        self.prog_lang = prog_lang
# The above line helps in assigning more attributes to our subclass and it also helps in grabbing the first, last and pay from the Employee Class itself.
dev_1 = Developer('Kartikey', 'Hebbar', 50000, 'Permanent', 'Python')
dev_2 = Developer('Ankit', 'Akash', 30000, 'Temporary', 'C')
# print(dev_1.email)
# print(dev_2.email)
# dev_1.apply_raise()
# print(dev_1.pay)

class Manager(Employee):
    raise_amount = 1.13
    def __init__(self, first, last, pay, status, employees=None):
        super().__init__(first, last, pay, status)  #Employee().__init__(self, first, last, pay) -->This is used for Multiple Inheritance
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

mgr_1 = Manager('Vijayakumar', 'MR', 100000, 'Executive', [dev_1])

print(issubclass(Manager, Employee))        #Tells that Manager is a subclass of Employee.
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
#
#
# print(dev_1.prog_lang)
# print(dev_2.prog_lang)
# print(help(Developer))    # Provides a good amount of info about the class and everything on the console
#print(isinstance(dev_1, Developer))        #Checks whether the object is an INSTANCEof the given class.
