List = ["onion", "Garlic","chili","spinch"]
#We have to print only onion and chili
i = 1 # i is index which starts with 1
for item in List:
    if i % 2 is not 0:
        print(f"{item} available in market")
    i += 1
#In short
for index, item in enumerate(List):#Index starts with zero
    if index % 2 == 0:
        print(f"{item} has available in market!")

#print list using join keyword
J = " and ".join(List)
print(J, "are the vagetables!")
