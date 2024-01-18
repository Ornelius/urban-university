def test(*args, **kwargs):
    i = 0
    j = 0
    print('Type args: ', type(args))
    for arg in args:
        i += 1
        print('Type: ', type(arg))
        print('parameter ', i, ': ', arg)
    print('Type kwargs: ', type(kwargs))
    for key, value in kwargs.items():
        j += 1
        print('Type: ', type(value))
        print('parameter ', j, ': ', key, "=", value)


def increment():
    number_of_task[0] += 1
    return number_of_task[0]


number_of_task = [0]
default_string = "_" * 30

print(default_string)
print("Задание №", increment(), ": ")
test(1, 3, 'list', True, [1, 2, 3, 4, 5, 6, 7], town='Москва', fruit='Яблоко')


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n - 1)
    return n * factorial_n_minus_1


print(default_string)
print("Задание №", increment(), ": ")
print('Факториал: ', factorial(8))
