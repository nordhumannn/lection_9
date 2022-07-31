# Task:
# Создайте декоратор, который зарегистрирует декорируемую функцию в
# списке функций, для обработки последовательности.

functions = []


def my_functions(func):
    """
    registers a function in the "functions" list
    """
    functions.append(func)
    return func


@my_functions
def summ(a, b):
    return a, b


@my_functions
def div(a, b):
    return a / b


print(my_functions)
