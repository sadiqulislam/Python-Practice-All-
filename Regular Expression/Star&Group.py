import re

pattern= r"bread(egg)*"

if re.match(pattern,"breadeggeggegg"):
    print("Match")



pattern2 = r"bread(egg)*bread"

if re.match(pattern,"breadeggeggeggeggeggbread"):
    print("Match")