# For Loop Iteration In List:

list1 = ["Shishir", "Saad", "Nirjona", "Ratul", "Farhan"]

for item in list1:
    print(item)

# Iteration In Dictionary:

dict1 = {"Shishir": 23, "Saad": 2, "Nirjona": 12, "Rataul": 13}

for item, age in dict1.items():   # .items() is a function to access in dictonary
    print(item, age)

# Iteration List Of List:

list2 = [["Shishir", 23], ["Saad", 2], ["Nirjona", 12], ["Ratul", 13], ["Farhan", 5]]

for name, age in list2:
    print(f"Name Is {name} and Age Is {age}")
for name, age in enumerate(name,start=1):
    print(name,age)
