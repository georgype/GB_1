num = int(input("Введите количество товаров "))
goods =[]
for i in range(num):
    name = input('Введите название товара ')
    cost = int(input('Введите цену товара '))
    qty = int(input('Введите количество товара '))
    meas = input('Введите единицу измерения товара ')
    d = {"название": name, "цена": cost, "количество": qty, "ед.изм.": meas}
    goods.append((i + 1, d))
print(*goods, sep='\n')
# Аналитика
d = {}
for i in goods:
    for j in range(4):
        param = list(i[1].keys())[j]
        list_val = d.get(param, [])
        list_val.append(i[1][param])
        d[param] = list_val
print(d)



