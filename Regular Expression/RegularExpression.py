import re

pattern= r"sishishir2015@gmail.com"

if re.match(pattern,"@gmail.com"):
    print("Match Found")

else:
    print(None)

pattern2 = r"egg"

if re.search(pattern2,"eggbaconeggbaconegg"):
    print("Match Found")

else:
    print("Not Match")

if re.findall(pattern2,"eggeggbaconeggbacon"):
    print("Match Found")

else:
    print("Not Found")


print(re.findall(pattern2,"eggbaconeggbaconeggegg"))