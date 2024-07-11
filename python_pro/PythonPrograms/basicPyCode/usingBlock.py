#Using block to open python flie
with open("SampleFile.txt") as f:#Instead of using open and close keywords block is used
    line = f.readlines()
    print(line)


f= open("SampleFile.txt", "rt")

content = f.read()
print(content)
f.close()