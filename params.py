# 2023/10/07 00:00|Самостоятельная работа по уроку "Распаковка параметров и параметры функции"
from test import a


def print_params(a=1, b="string", c=True):
    print('a: ', a, " b: ", b, " c: ", c)


print_params()
print_params(3,4,5)
#print_params(3,4,5, 6) # не работает
print_params(b = 25)
print_params(c = [1,2,3])

valuse_list = [1,"string", True]
values_dict = {'a': 1, 'b': "string", 'c':True}


print_params(*valuse_list)
print_params(**values_dict)

values_list_2 = [True, 6]
print_params(*values_list_2, 42)