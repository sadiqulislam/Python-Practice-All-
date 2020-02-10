import re

string = "My Name Is Shishir,Hi! I Am Shishir"

print(string)

pattern = r"Shishir"

newstring = re.sub(pattern,"Presence",string)

print(newstring)