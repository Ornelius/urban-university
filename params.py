# 2023/10/07 00:00|Самостоятельная работа по уроку "Распаковка параметров и параметры функции"

def print_params(a=1, b="string", c=True):
    print('a: ', a, " b: ", b, " c: ", c)


print_params()
print_params(3,4,5)
print_params(3,4,5, 6) # не работает
print_params(b = 25)
print_params(c = [1,2,3])