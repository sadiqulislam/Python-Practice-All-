file = open("Shishir.txt",'r')

content = file.read()
print(content)
file.close()

file = open("Shishir.txt","wr")

file.write("I Am The Boss")
# content = file.read()
print(file.read())
file.close()
