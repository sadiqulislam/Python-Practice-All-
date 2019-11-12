file5 = open('Shishir.txt')

print(file5.tell())
content = file5.readline()
print(file5.tell())
content = file5.readline()
print(file5.tell())
file5.seek(15)
print(content)
print(content)

file5.close()