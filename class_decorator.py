# Task:
# 3) Предположим, в классе определен метод __str__, который возвращает
# строку на основании класса. Создайте такой декоратор для этого метода,
# чтобы полученная строка сохранялась в текстовый файл, имя которого
# совпадает с именем класса, метод которого вы декорировали.


def decorator(func):
    """
    writes the result of the __str__ method
    execution to a file whose name is the
    name of the current class
    """
    count = 1

    def inner(args):
        nonlocal count
        with open(args.__class__.__name__ + '.txt', 'a') as f:
            f.write(f'{count}: ' + func(args) + '\n\n')
            f.close()
        count += 1
        return func(args)
    return inner


class Student:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    @decorator
    def __str__(self):
        return f'{self.name} {self.surname}, {self.age}'


st_1 = Student('A', 'D', 19)
st_2 = Student('J', 'F', 29)
st_3 = Student('V', 'D', 18)
st_4 = Student('E', 'T', 21)
st_5 = Student('K', 'R', 23)

print(st_1)
print(st_2)
print(st_3)
print(st_4)
print(st_5)

# Output:
# 1: A D, 19
#
# 2: J F, 29
#
# 3: V D, 18
#
# 4: E T, 21
#
# 5: K R, 23

