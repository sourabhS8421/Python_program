#f = open("SampleFile1.txt","a")# a = append
#a=f.write("Sourabh you have to wake up early in the morning!")
#print(a)
#f.close()

#f = open("SampleFile1.txt","w")# a = append
#f.write("Sourabh you have to wake up early in the morning!")

#f.close()

#Handle read and write both
f = open("SampleFile1.txt","r+")#r+ is both read and write
print(f.read())#run only this line first -> read operation
f.write("Thank you!")
