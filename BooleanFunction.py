username = "Admin"
password = "12345"

user_username = str(input("Enter Your Username: "))
user_password = str(input("Enter Your Password: "))
if user_username == "Admin" and user_password == "12345":

    print(f"Suucessfully LOgged In As {username}")

else:
    print("Username Or Password Invalid")
