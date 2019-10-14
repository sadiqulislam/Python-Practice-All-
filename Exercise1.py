#For Loops :

list1 = [ ]
print("How Much List You Want: \n")
count = int(input())
print("Enter Your List Here: \n")
for i in range(count):
    user = list(input())
    list1 = list1.append(user)

print(list1)