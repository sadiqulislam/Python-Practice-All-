cs_course ={'Math','Physics','Chemestry','History'}
art_course ={'Math','History','Design','Psychology'}

#Interset "Thing In Common":

print(cs_course.intersection(art_course))
print(type(cs_course))

#Difference "Thing In Uncommon"

print (cs_course.difference(art_course))
print(art_course.difference(cs_course))

#Union "Adding Two Sets"

print (cs_course.union(art_course))
empty_sets = set()
print(type(empty_sets))

