def phebonice(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return phebonice(n-1)+phebonice(n-2)
    
num = int(input("enter the number"))
print(phebonice(num))