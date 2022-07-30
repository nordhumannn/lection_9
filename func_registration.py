functions = []

def my_functions(func):
    functions.append(func)
    return func

@my_functions
def summ(a, b):
    return a, b

@my_functions
def div(a, b):
    return a / b

print(my_functions)
