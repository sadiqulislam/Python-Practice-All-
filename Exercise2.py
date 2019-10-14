

while(True):
    print("Enter Your Number:\n")
    num = int(input())
    if (num<100):
        print(f"You Entered {num}")
        continue
    elif (num>=100):
        print(f"You Entered {num} Which Is Greater Than 100! End")
        break
        #num = num+1