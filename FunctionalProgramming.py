def function1(x):
    return x + x


def function2(func, arg):
    return func(func(arg))


print(function2(function1, 10))
