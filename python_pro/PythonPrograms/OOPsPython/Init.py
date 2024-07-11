class Student:#every class must have constructor
    pass

    #Constructor of class student
    def __init__(self,Name,Age,Course): #parameterized constructor
        self.name = Name
        self.age = Age
        self.course = Course
        
kiran = Student("Kiran",20,"BBA")
print(kiran.name)
print(kiran.age)
print(kiran.course)

