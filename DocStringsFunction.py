#Doc String In Function:

def function1(a,b):
    """This Function Will Return Average Value Of Two Numbers"""

    average = (a+b)/2
    return average

v = function1.__doc__
print(v)