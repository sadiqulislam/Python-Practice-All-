import re

string = "HFishaioiosedjgiosjiogioseghiouidbugdui"

pattern = r"H.i"

if re.match(pattern,string):
    print("Match Found")

else:
    print("Not Found")