def demo1():
    #We can print a function using another function
    def test1():
        print("Hello I'm Sourabh")

    #func1 is new function which store test function in it
    func1 = test1
    #Afer deletion of test function, the body of test function saved in func1 
    del test1
    func1()

def demo2():#If this code not run, remove demo2 function then run this code
    def funcret(num):
        if num == 0:
            print("You have inputed 0 as argument")
        else:
            print("You have inputed other than zero as argument")

    a = funcret(0)
    print(a)

#We can add function as argument in another function
def demo3():
    def executor(func): #func is the function which present as a argument in executor function
        func("Sourabh")

    executor(print)

#Function decorator
