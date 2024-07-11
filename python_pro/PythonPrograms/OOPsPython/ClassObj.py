#Class
"""class Hostel:
    pass  #If we want to leave blank this template, use pass,it does not show error
student = Hostel()

student.name = "sourabh"
student.age = 20

print(student.name)"""

#Instance variables

class Employee:
    salary = 50000
    
#There are two instances 1.sourabh & 2.suyash
sourabh = Employee()
suyash = Employee()

sourabh.name = "sourabh"
sourabh.salary = 70000
print(Employee.salary)
#property of class does not change even after updating salary of class Employee
#Sourabh.salary created their own instance variable
sourabh.id = 22119
sourabh.age = 20

suyash.name = "suyash"
suyash.id = 56188
suyash.age = 18
suyash.salary

print(sourabh.age)
print(sourabh.__dict__)
print(suyash.salary)