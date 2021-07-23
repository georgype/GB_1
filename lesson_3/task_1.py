def my_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

a, b = int(input('Введите делимое число ')), int(input('Введите делитель '))
print(my_div(a, b))