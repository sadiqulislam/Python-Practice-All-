num = input("Please Enter Your Result:")

result = int(num)

if result>=0 and result <=30:
    print("You Get F Grade")

elif result>=31 and result <=49:
    print("You Get E Grade")

elif result>=50 and result <=59:
    print("You Get D Grade")

elif result>=60 and result <=69:
    print("You Get C Grade")

elif result>=70 and result <=79:
    print("You Get B Grade")

elif result>=80 and result <=100:
    print("You Get A Grade")

else:
    print("Unknown Number!")