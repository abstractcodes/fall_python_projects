name = input("Enter name of the person: ")
rent = input("Enter receipt amount of the person: ")
print("*"*40)
for index in range(10):
    print("*",end="")
    if index == 0:
        print(" Name="+name,end = "")
        print(" "*20,end="")
        print(" Rent="+rent,end = "")
    print(" "*38,end="")
    print("*")
print("*"*40)