class college:
    total_intake = 70

    #constructor
    def __init__(self,Branch,Id,Faculty):
        self.branch = Branch
        self.id = Id
        self.faculty = Faculty
    
    #Static method
    @staticmethod
    def ratings(int):
        print("Total ratings are 10 out of "+ int)
    
    #Method
    @classmethod
    def ChangeIntake(cls,newIntake):
        cls.total_intake = newIntake

#Class subject inherited the properties of class college
class subject(college): #Single inheritance
    def __init__(self,Branch,Id,Faculty,Language):
        self.branch = Branch
        self.id = Id
        self.faculty = Faculty
        self.language = Language
       
#Objects     
cse = college("Computer Science Engineering",200,12)
it = college("Information Technology",320,8)

print(f"Branch name is {cse.branch}. Branch ID:{cse.id}. Total faculty:{cse.faculty}")
cse.ChangeIntake(120)#Error
print(f"Branch name is {it.branch}. Branch ID:{it.id}. Total faculty:{it.faculty}")
it.ChangeIntake(60)#Error

aiml = subject("artificial intelligence & machine learning",2217,10,"Python")
print(f"Branch name is {aiml.branch}. Branch ID:{aiml.id}. Total faculty:{aiml.faculty}. Language required:{aiml.language}")
