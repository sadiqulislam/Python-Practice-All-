#Traditional Way To Swap Two Numbers:

a = 10
b = 5

# 10
temp = a
a= b
b = temp
print(a,b)

#In Python Way:

a1 = 100
b1 = 500
a1,b1 = b1, a1
print(a1,b1)