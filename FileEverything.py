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