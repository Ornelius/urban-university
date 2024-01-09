# 2023/10/05 00:00|Домашняя работа по уроку "Пространство имен и способы вызова функции"

a, b, c = 8, 9, 10


def test():
    a, b = 5, 6
    print('a: ', a, ' b: ', b)


def test2():
    a, b, c = 5, 6, 7
    print('a: ', a, ' b: ', b, ' c: ', c)


def test3(a, b, c):
    print('a: ', a, ' b: ', b, ' c: ', c)


test()
test2()
test3(a, b, c)
