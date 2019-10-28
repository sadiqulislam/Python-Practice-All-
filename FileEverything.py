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