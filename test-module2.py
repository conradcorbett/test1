
class Employee: #This is the class

    raise_amount = 1.05

    def __init__(self, first, last, pay): #this is a method, special type init
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self): #this is another method, a method is a function associated with a class
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000) #emp_1 is an instance
emp_2 = Employee('Test', 'Employee', 60000) #emp_2 is an instance

print(emp_1.fullname()) #emp_1 is instance, fullname is method
print(Employee.fullname(emp_1)) #using the class name, need to manually pass instance as an arguement

print(Employee.raise_amount)
print(emp_1.raise_amount)

print(emp_1.raise_amount)
