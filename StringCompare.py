str1 = input("Please Enter Your Name: ")
str2 = input("Enter Another Name: ")
name1 = str(str1)
name2 = str(str2)

if name1 == name2 :
    print("Same name")

elif name1.lower() == name2.lower():
    print("Same Name")

elif name1.upper() == name2.upper():
    print("Same Name")

else:
    print("Different Name")