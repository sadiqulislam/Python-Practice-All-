#Creating My Dictonary As A Practice:

presence = {"Mutable":"Changable",
            "Immutable":"Not Changable",
            "Presence":"Present",
            "CAO":"Computer Architecture & Organization",
            "NLP":"Natural Language Processing",
            "ML":"Machine Learning",
            "AI":"Artificial Intilligence",
            "OS":"Operating System",
            "GPS":"Global Positioning System",
            "ALU":"Arithmetic Logic Unit",
            "CPU":"Central Processing Unit",
            "GPU":"Graphical Processing Unit",
            "RAM":"Random Access Memory",
            "CD":"Cyclic Disk",
            "IR":"Ifrared Ray",
            "SAD":"System Ananlysis And Design",
            "OP":"Over Powered",
            "GG":"Good Going",
            "FBI":"Federal Burue Of Investigation",
            }

print("Enter Your Word From This List Only")
print(["Mutable",
       "Immutable",
       "Presence",
       "CAO",
       "NLP",
       "ML",
       "AI",
       "OS",
       "GPS",
       "ALU",
       "CPU",
       "GPU",
       "RAM",
        "CD",
       "IR",
       "SAD",
       "OP",
       "GG",
       "FBI",
       ])

word = input()
print(presence.get(word))