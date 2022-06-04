class employee:

    num_of_emps=0  # class variables
    raise_amount=1.04

    def __init__(self,first,last,pay): # instance variables
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'

        employee.num_of_emps +=1

    
    def fullname(self):
        return f'{self.first}  {self.last} '

    def __repr__(self):
        return "employee ('{}','{}','{}')" .format(self.first,self.last,self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.email)

emp_1=employee('chege','waweru',100000)
emp_2=employee('corey','schafer',30000)
print(emp_1)
print(emp_1.__str__())
print(emp_2.__str__())
print(emp_2.__repr__())
print(emp_1.__repr__())

'''
there are so many special methods and its upon you to research which you need to use
in any case programming is all about syntax
e.g __add__ , __len__ ... the list is endless...

'''
