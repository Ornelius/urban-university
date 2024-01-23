def test_function():
    print(__name__)

    def inner_function():
        frame = inner_function.__qualname__.split(".")
        print("Я в области видимости: " + frame[0])

    inner_function()


test_function()

# inner_function() - Функция не определена! Вызова не произойдет
