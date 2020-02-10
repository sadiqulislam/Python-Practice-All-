import re

string = "152AABED"

pattern = r"[0-9][0-9][0-9][A-D][A-Z][A-Z][A-Z][A-Z]"

if re.search(pattern,string):
    print("Match")