def add(x):
    return x + 10


list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

result = list(map(add, list1))

print(result)


# Map With Lambda Function

list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = list(map(lambda x: x*2, list3))

print(result)