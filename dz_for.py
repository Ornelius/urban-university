# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for car in cars:
    print("Я езже на автомобиле марки " + car)


i = 1
car_count = 0
cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for car in cars:
    print("Я езжу на автомобиле марки " + car)
    if i >= 2:
        car_count += 10
    print("car_count: ", car_count)
    i += 1

