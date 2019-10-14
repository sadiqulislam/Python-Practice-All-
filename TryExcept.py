print("Enter The First Number: \n")
num1 = input()
print("Enter The Second Number: \n")
num2 = input()

try:
    summation = int(num1) + int(num2)
    print(f"The Sum Of {num1} And {num2} Is ",summation)

except Exception as error:
    print(error)
    print("You Have Entered Wrong Input!")

print("Life Is Beautiful")