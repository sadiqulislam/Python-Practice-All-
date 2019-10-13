# File Handling


#Read
file1 = open("Shishir.txt","wb")
print(file1.name)
print(file1.mode)
file1.write(bytes('I am The Presence',"UTF-8"))
file1.write(bytes("I Am A Python Developer","UTF-8"))
print(file1,end="\n")
file1.close()

#Write:

file1 = open('Shishir.txt',"r+")
t_to_r = file1.read()
print(t_to_r)
file1.close()