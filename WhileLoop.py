 #While Loop:
x = 0
while x<=5:
    print(x)
    x+=1

#Taking User Input:

num =input("Please Enter A Number: ")
num = int(num)
x = 0
while x<=num:
    print(x)
    x+=1

#infinite Loop With Break Key:

x = 1
while True:
    print(x)
    x+=1

    if x>=10:
        break

#Continue Key:

x= 1

while x < 20:
    x += 1
    if x % 2==0:
        continue
    print(x)
