# решение через **
def my_func_1(x, y):
    return x ** y


# Решение через цикл
def my_func_2(x, y):
    result = 1
    while y:
        result /= x
        y += 1
    return result


x = float(input('Введите число '))
y = int(input('Введите степень '))
print(my_func_1(x, y))
print(my_func_2(x, y))
