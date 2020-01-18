# Basic Function Call:
def welcome():
    x = 'Welcome To Python'
    print(x)


welcome()


# Function Call With Iterartion:

def hello():
    x = "Hello World"
    for wel in x:
        print(x)


hello()


def hello_2():
    x1 = 'Shishir'
    for name in x1:
        print(x1)


hello_2()


# Parameter Passing:

def new_name(name):
    name_1 = name
    name_2 = name
    print("Welcome,{}".format(name_1.lower()))
    print("Welcome {}".format(name_2.upper()))


new_name('SHIShIR')
new_name("The_Presence")


# Positional Parameter Passing:

def info(name, age, phone):
    print("Name={},Age={},Phone={}".format(name, age, phone), sep='|||')


info(name='Shishir', age='23', phone='01681986940')


# Keyword Argument:

def personal_info(p_name, p_age, p_country='Bangladesh'):
    print(p_name, p_age, p_country)


personal_info(p_name='Taylor', p_age='23', p_country='US')  # Keyword Argument
personal_info('Alam', 30)  # Positional Argument
personal_info(p_name='Salam', p_age=30)  # Keyword Argument With Default Value


# Function Return Value:

def sqr1(num):
    return num * num


print(sqr1(2))


# Another Example:

def get_name(first_name, last_name):
    return "First Name={} , Last Name ={}".format(first_name, last_name)


print(get_name('Bill', 'gates'))


def get_name2(f_name, l_name):
    return "{} {}".format(f_name, l_name)


print(get_name2('Steve', ('Jobs')))


def get_name3(f3_name, l3_name):
    return f'{f3_name} {l3_name}'


print(get_name3('The', 'Presence'))


def get_name4(f4_name, l4_name):
    return f4_name + " " + l4_name


print(get_name4('Gutsy', 'Warrior'))


# Optional Arguement:

def opt_name(first_name, last_name, middle_name=''):
    complete_name = first_name + " " + last_name
    if middle_name:
        complete_name += " " + middle_name
    return complete_name


print(opt_name('Mohammad', 'Sadiqul', 'Islam'), sep=' ')
print(opt_name('Md', 'Sadiqul'), sep=' ')
