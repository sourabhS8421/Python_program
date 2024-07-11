import time
#Calculating running time
init1 = time.time()
k = 0
#change the value 51 to something
while(k<51):
    print("I'm sourabh!")
    time.sleep(2) #It print output after every 2 seconds
    k += 1
print("while loop ran in ",time.time() - init1,"seconds")

init2 = time.time()
#Change the value 89 to something
for i in range(89):
    print("I'm sourabh!")
print("for loop ran in", time.time() - init2,"seconds")

#Printing local time
LocalTime = time.asctime(time.localtime(time.time()))
print(LocalTime)


