class Student:
    year = "Third year"

    def KiranDetails(self): 
        print(f"There is a boy named {self.name} & currently in {self.year}, age {self.age},has salary {self.salary}.")

kiran = Student() # call of class Student

kiran.name = "Kiran"
kiran.age = 20
kiran.salary = 60000
print(kiran.KiranDetails())#Method calling