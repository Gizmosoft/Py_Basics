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

emp_1 = Employee('Kartikey', 'Hebbar', 1000000, 'Permanent')
emp_2 = Employee('Ankit', 'Akash', 900000, 'Temporary')

# print(emp_1.first)
# print(emp_2.first)
# print(emp_1.last)
# print(emp_2.last)
# print(emp_1.pay)
# print(emp_1.email)
# print(emp_1.status)
# print(emp_2.status)
# print(emp_1.fullname())
# print(emp_1.all())

# print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.all())
print(emp_1.__dict__)

emp_2.raise_amount = 1.05
emp_2.apply_raise()
emp_2.pay
print(emp_2.all())
