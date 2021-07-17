a = int(input('Введите количество км '))
b = int(input('Введите требуемое количество км '))
c = 1
while a < b:
    a *= 1.1
    c += 1
print(c)