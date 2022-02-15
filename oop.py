'''
class dog:
    species='cannis familiaris'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,sound):
        return f"{self.name} says {sound}"

buddy=dog('buddy',4)
simba=dog('simba',10)
print(simba.name)
print(simba.age)
print(buddy.age)
print(buddy.name)
#print(simba.description())
print(simba.speak('woof woof'))
print(buddy.speak('boow boow'))
print(simba)
'''

#parent classes and child classes
#child classes inherit from parent classes
'''
class dog:
    species='Cannis familiaris'
    def __init__(self,name,age,breed):
        self.age=age
        self.name=name
        self.breed=breed

    def __str__(self):
        return f"{self.name} is {self.age} years old and is a {self.breed}"
    def speak(self,sound):
        return f"{self.name} says {sound}"

miles=dog('miles',2,'rottweiler')
morales=dog('morales',12,'husky')
simba=dog('simba',5,'bulldog')
print(morales)
print(morales.speak('woof woof'))

class bulldog(dog):
    pass
class rottweiler(dog):
    pass
class husky(dog):
    pass

puppy=bulldog('puppy',3)
type(puppy)
isinstance(miles, dog)
'''

# another example
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

    def apply_raise(self):
        #self.pay=int(self.pay * 1.04) this wont work coz raise amount should be class variable
        self.pay=(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #automated new employee creator
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

#static methods
    @staticmethod
    def is_work_day(day):
        if day.weekday()==5 or day.weekday==6:
            return False
        return True

import datetime
my_date=datetime.date(2022,2,11)
print(employee.is_work_day(my_date))

#inheritance and creating subclasses
class developer(employee):
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang=prog_lang
dev_1=developer('david','gibu',70500,'python')
dev_2=developer('ken','mwas',97866,'kotlin')
print(dev_2.email)
print(dev_1.email)
print(dev_1.prog_lang)

class manager(employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())

dev_1=developer('david','gibu',70500,'python')
dev_2=developer('ken','mwas',97866,'kotlin')
mgr_1=manager('sue','smith',90000,[dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()






#create a new employee from a given data
#manually
emp_str_1='john-doe-300233'
emp_str_2='steve-smithy-224324'
emp_str_3='pero-fireth-342332'
new_emp_1=employee.from_string(emp_str_1)
print(new_emp_1.email)
#first,last,pay=emp_str_1.split('-')
#new_emp_1=employee(first,last,pay)


employee.set_raise_amount(1.05)
print(employee.raise_amount)

emp_1=employee('chege','waweru',100000)
emp_2=employee('corey','schafer',30000)
print(emp_1.fullname())


