courses_1 = ['Physic','Chemestry','CSE']
print(courses_1)

print(len(courses_1))

print(courses_1[0:2])

courses_1.append('SWE')
print(courses_1)
courses_1.insert(4,'Algorithm')

print(courses_1)

courses_2 =['Math','Biology','Bangla']

courses_1.extend(courses_2)

print(courses_1)

print(len(courses_1))

#Remove From The List

courses_3 = ['Math','Physic','Chemistry','Biology']

courses_3.remove('Math')

print(courses_3)

courses_3.pop() #By Default Its Remove The Last Value

print(courses_3)

#Reverse The List

courses_4 = ['Robotics','Ethics','AI','Data','Embeded','Wirless']

courses_4.reverse()
print(courses_4)

#Sorting The Lists In Ascending Order

courses_4.sort()
print(courses_4)

letter = ['a','g','b','w','i','d','x']

letter.sort()
print(letter)

#Sorting The Lists In Descending Order

letter = ['a','g','b','w','i','d','x']

letter.sort(reverse=True)
print(letter)

courses_4.sort(reverse=True)
print(courses_4)

#Sorting By Calling Sorted Function

number = ['3','4','1','5','2']

sort_number = sorted(number)
print(sort_number)

#Minimum And Maximum Of List:

number_2 = [1,2,3,4,5]

print(min(number_2))
print(max(number_2))
print(sum(number_2))