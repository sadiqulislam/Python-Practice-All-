import re

string = "152AABED"

pattern = r"[0-9][0-9][0-9][A-D][A-Z][A-Z][A-Z][A-Z]"

if re.search(pattern,string):
    print("Match")



pattern2 = r"^[a-z][@][a-z][.][a-z].$"

string="sishisir@gmail.com"

if re.match(pattern,string):
    print("Match")