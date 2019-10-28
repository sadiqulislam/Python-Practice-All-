#File Basic :

#File Mode:

'''
"r" = Open File For Reading -Default
"w' = Open File For Wrighting
"x" = Creates File If Not Exists
"a" = Add More Content To the File At the End- Append
"t" = Text Mode -Default
"b" = Binary
"+" = Read And Write
'''

#File Opening For Reading:

file = open("Shishir.txt","r")

content = file.read()
print(content)

file.close()

#File Iterate OR Print Letter:

file2 = open("Shishir.txt")
content2 = file2.read()

for line in content2:
    print(line)

file2.close()

#File Iterate OR Print Line By Line:

file = open("Shishir.txt")

for line2 in file:
    print(line2,end="")

file.close()

#ReadLine & ReadLines Function:

file = open("Shishir.txt")
print(file.readline())      #Print Line
print(file.readline())
file.close()

file = open("Shishir.txt")
print(file.readlines())   #Print As A Lists
file.close()


#File Writing:

file3 = open("Shishir2.txt","w")

file3.write("Shishir Is A Good Guy")

file3.close()

#Appending:

file4 = open("Shishir2.txt","a")
file4.write("I am Lucky Charm\n")
file4.close()

#Handle Read And Write Both:

file5 = open("Shishir2.txt","r+")
s = file5.read()
file5.write("Thanks")

print(s)

file5.close()