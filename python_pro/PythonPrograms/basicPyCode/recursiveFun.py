#Claculating factorial of user defined number 
#number = int(input("Enter the number"))
def iterativeapp(n):
    #f = 1
    for i in range (n):#No need to write 'i+1', value of i is automatically increase!
        try:
            f = f * (i+1)
            return f
        except Exception as e:
            print(e)
    

def recursiveapp(m):
    if m == 1:
        return 1
    else:
        return m * recursiveapp(m-1)

number = int(input("Enter the number"))
print(iterativeapp(number))
print(recursiveapp(number))