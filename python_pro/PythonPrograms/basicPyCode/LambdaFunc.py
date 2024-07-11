#One linear function or anonnymous function
def Add(x,y):
   return x+y

Lambda = lambda x,y:x+y#Function in one line
                    #Used when we don't want to create function

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
result=Add(num1,num2)
print(result)
print(Lambda(3,4))