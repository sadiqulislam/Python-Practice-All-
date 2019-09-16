courses = ['Math','Physics','Chemestry','Arts','History']

for course in courses:
    print(course)

#Print With Index Number:

for index , course in enumerate(courses,start=1):
    print(index,course)