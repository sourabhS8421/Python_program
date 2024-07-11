f = open("SampleFile.txt","rt")
#content = f.read()
#print(content)
#f.close()

#print only one line
#print(f.readline())
#print(f.readline())

#print(f.tell())  #prints the f pointer location
print(f.readline())
#print(f.tell())
print(f.seek(11))#used to change the location of file pointer (f) starting location
print(f.readline())
#print(f.tell())
f.close()