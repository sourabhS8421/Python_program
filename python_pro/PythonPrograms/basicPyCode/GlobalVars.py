globv = 20

def function1(n):
    
    #globv= 40#Global variables can't be changed in function unless 'global'keyword
    global globv#By using this we can change the value of global variable
    globv = globv + 10
    print(n,"I have money!")
    print("The value of w is:",globv)

#function1("Hello there")
def sourabh():
    globv = 23
    def ann():
        global globv
        globv = 21
    print("Before calling ann",globv)
    ann()
    print("After calling ann",globv)
sourabh()
print(globv)




