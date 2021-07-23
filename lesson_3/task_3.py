def my_func(a, b, c):
    return sum([a, b, c]) - min(a, b, c)


a, b, c = [int(input('Введите число ')) for i in range(3)]
print(my_func(a, b, c))
