#static memory allocation
#we can only add limited arguments as we defined in function
def exam(a,b,c,d):
    print(a,b,c,d)

exam("upsc","mpsc","ssb","gate")

#Dynamic memory allocation
#We can add as many as arguments we want
def test(*args):
    print(args)

test("sourabh","sadik","kiran","suyash","harshad","soham")

