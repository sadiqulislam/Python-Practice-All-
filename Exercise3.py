my_number = 71
no_of_guess= 9
guess = 1
for guess in  range (1,no_of_guess):
     print("Enter Your Number: \n")
     user = int(input())
     if (user>my_number):
        if (guess<=no_of_guess):
            print("Lower You Number for Exact Number")
            print(f"You Attempt {guess}")
            left = no_of_guess - guess
            print("You Left ",left,"Attempt")
            guess = guess +1
            if (guess==no_of_guess):
                print("Game Over")
                break
     elif(user<my_number):
         if (guess <= no_of_guess):
            print("Increase Your Number")
            print(f"You Attempt {guess}")
            left = no_of_guess - guess
            print("You Left ", left, "Attempt")
            guess = guess + 1
            if (guess == no_of_guess):
                print("Game Over")
                break


     else:
         print("Congratulations")
         print(f"You Find The Number At {guess} Attempt ")
         left = no_of_guess - guess
         print("You Left ", left, "Attempt")
         guess = guess + 1
         break
