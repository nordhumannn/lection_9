def simple_decorator(func):
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

    @simple_decorator
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
