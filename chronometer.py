# Task:
# Создайте декоратор с параметрами для проведения хронометража работы
# той или иной функции. Параметрами должны выступать то, сколько раз нужно
# запустить декорируемую функцию и в какой файл сохранить результаты
# хронометража. Цель - провести хронометраж декорируемой функции.

import time


def chronometer(number, file_name):
    """
    calls the decorated function 'number' times
    (specified in the parameters) and writes the
    output to a file with the name specified
    in the parameters
    """
    count = 0
    start = time.time()
    while count < number:
        def wrapper(func):
            def inner(*args):
                return func(*args)
            return inner

        end = time.time()

        with open(file_name + '.txt', 'w') as f:
            f.write(f'Function passed: {str(number)}, time: {str(end - start)}\n')
            f.close()
            count += 1
    return wrapper

# --------------------------------------------------------------------------------------------


def chronometer(number, file_name):
    def wrapper(func):
        def inner(*args, **kwargs):
            start = time.time()

            for i in range(number):
                res = func(*args, **kwargs)

            stop = time.time()
            with open(file_name + '.txt', 'w') as f:
                f.write(f'{start} - {stop}: ---> {stop - start}')
                f.close()
            return res
        return inner
    return wrapper


@chronometer(5, 'test')
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))

