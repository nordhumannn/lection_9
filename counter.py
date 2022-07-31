# Task:
# Создайте декоратор, который будет подсчитывать, сколько раз была
# вызвана декорируемая функция.

def counter(func):
    """
    counts and returns how many times
    the function has been called 
    """
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        res = f'Result: {func(*args, **kwargs)}, count: {count}'
        return res
    return inner


@counter
def mul(x, y):
    return x * y


print(mul(2, 3))
print(mul(2, 3))
print(mul(2, 3))
print(mul(2, 3))
