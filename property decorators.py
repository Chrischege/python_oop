# e.g getters , setters , deleter...e.t.c
#they allow us to define class methods that we can access like attributes
'''
if you noticed the email only depends on the first and last and if those were to change then it would not change buh stick to the previous values
'''
class employee:

    num_of_emps=0  # class variables
    raise_amount=1.04

    def __init__(self,first,last): # instance variables
        self.first=first
        self.last=last
    
        employee.num_of_emps +=1
    
    @property
    def email(self):
        return '{}.{} @email.com'.format(self.first,self.last)

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1=employee('corey','schafer')


print(emp_1.fullname)
print(emp_1.email)


