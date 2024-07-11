#If I don't want to use self
class Employee:
    salary = 40000  #Instance variable of class

    def __init__(self) -> None:
        pass
    
    #changing instance variable of class within the class. CHANGES APPLY TO ALL
    @classmethod    #Used to change instance variable of the class
    def change_salary(cls,newsalary):   #so that everyone can use new instance variable i.e. salary
        cls.salary = newsalary

sita = Employee()   #sita is Object of class Employee
ram = Employee()    #ram is Object of class Employee
shyam = Employee()  #shyam is object of class Employee

#we can change instance variable of class in 3 ways
shyam.salary = 20000    #NEW instance variable of object
print(shyam.salary)

ram.change_salary(50000) #calling changed instance variable of class   
print(ram.salary)

Employee.salary = 70000 #changing instance variable of class
print(sita.salary)
