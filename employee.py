
class Employee:
    raise_amount = 1.2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay



    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay* Employee.raise_amount)

emp_1 = Employee('Xyz', 'abc', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print("current salary", emp_1.pay)
emp_1.apply_raise()
print("after raise, salary=" , emp_1.pay)