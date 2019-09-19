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