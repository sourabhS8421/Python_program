def harry(choice):
    print("You've choosen for harry\n")
    choice = int(input("Press 1 for exercise, press 2 for diet"))
    if choice == 1:
        f = open("lock_harExe.txt","r+")
        f.write("You've opened file of exercise for you succcessfully!")
    elif choice == 2:
        f = open("lock_harFood.txt","r+")
        f.write("You've opened file of diet for you successfully!")
        f.read()
    else:
        print("Invalid choice!")

def rohan(choice):
    print("You've choosen for rohan\n")
    choice = int(input("Press 1 for exercise, press 2 for diet"))
    if choice == 1:
        f = open("lock_rohExe.txt","r+")
        f.write("You've opened file of exercise for you succcessfully!")
    elif choice == 2:
        f = open("lock_rohFood.txt","r+")
        f.write("You've opened file of diet for you successfully!")
        f.read()
    else:
        print("Invalid choice!")

def hammad(choice):
    print("You've choosen for hammad\n")
    choice = int(input("Press 1 for exercise, press 2 for diet"))
    if choice == 1:
        f = open("lock_hamExe.txt","r+")
        f.write("You've opened file of exercise for you succcessfully!")
    elif choice == 2:
        f = open("lock_hamFood.txt","r+")
        f.write("You've opened file of diet for you successfully!")
        f.read()
    else:
        print("Invalid choice!")  

#If user press lock
def Lock(choice):
    print("For who you want to lock for?")
    choice = int(input("press 1 for Harry, press 2 for rohan, press 3 for Hammad\n"))
    if choice == 1:
        harry(choice)
    elif choice == 2:
        rohan(choice)
    elif choice == 3:
        hammad(choice)
    else:
        print("Invalid choice!")
#If user choose retrive
def Retrive(choice):
    print("For who you want to retrive for?")
    choice = int(input("press 1 for Harry, press 2 for rohan, press 3 for Hammad\n"))
    
    if choice == 1:
        harry(choice)
    elif choice == 2:
        rohan(choice)
    elif choice == 3:
        hammad(choice)
    else:
        print("Invalid choice!")
#Input from user lock or retrive?
print("Welcome to our gym!")
openion = int(input("press 1 for lock,press 2 for retrive\n"))
if openion == 1:
    Lock(openion)
elif openion == 2:
    Retrive(openion)
else:
    print("Invalid choise! Please re-enter again")