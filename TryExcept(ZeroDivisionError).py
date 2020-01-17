try:
    a = 10
    b = 0

    print(a/b)

except ZeroDivisionError:

    print("There Is Zero Division Error In The Code")




#Finally Block:

try:
    a = 20
    b = 10

    print(a/b)

except ZeroDivisionError:
    print("Error")

finally:
    print("It Will Print No Matter What")