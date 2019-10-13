student = {'Name': 'Shishir','Age': 23,'Course':['Robotics','Ethics']}

print(student)
print(student['Course'])
print(len(student))

#Sorting:
for key in sorted(student.keys()):
    print(key,student[key],sep=' > ')

#Dictonary Iteration For Show All Items In The Dictonary:

dict = {'a':97,'b':98,'c':99,'d':100}

for key,value in dict.items():
    print(key,value,sep='|')

#For Show Only Key

for key in dict.keys():
    print(key)

#For Show Only values:

for value in dict.values():
    print(value)


#New Example:

dictonary = {"Shishir":"Pizza","Saad":"Milk","Nirjona":"Chocolate"}

dictonary2 = {"Shishir":"Pizza","Ratul":{"Breakfast":"Porota","Launch":"Rice","Dinner":"Fish"}}

print(type(dictonary))
print(len(dictonary))
print(dictonary)
print(dictonary2)
print(dictonary2["Ratul"] ["Breakfast"])                    #Inside Dictonary Access
print(len(dictonary2))
print(len(dictonary2["Ratul"]))

del dictonary ["Shishir"]     # Delete A Diconary Key
print(dictonary)
