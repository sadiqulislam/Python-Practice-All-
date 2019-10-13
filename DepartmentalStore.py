sum = 0
count = 0
while (True):
    UserInput = input("Enter Your Item Price: \n")

    if UserInput != 'q':
        sum = sum + int(UserInput)
        print(f"Total So Far {sum}")


    else:
        print(f"Your Total Bill Is {sum}\n Thanks For Shopping")

        break