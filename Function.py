#Basic Function Call:

def welcome():
    x = 'Welcome To Python'
    print(x)

welcome()


#Function Call With Iterartion:

def hello():
    x="Hello World"
    for wel in x:
        print(x)

hello()


def hello_2():
    x1='Shishir'
    for name in x1:
        print(x1)
hello_2()


#Parameter Passing:

def new_name(name):
    name_1 = name
    name_2 = name
    print("Welcome,{}".format(name_1.lower()))
    print("Welcome {}".format(name_2.upper()))

new_name('SHIShIR')
new_name("The_Presence")

#Positional Parameter Passing:

def info(name,age,phone):
    print("Name={},Age={},Phone={}".format(name,age,phone),sep='|||')

info(name='Shishir',age='23',phone='01681986940')