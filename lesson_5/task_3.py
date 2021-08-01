with open('text_task_3.txt') as t:
    s = 0
    c = 0
    print('Имеют оклад менее 20 т.р.: ')
    for i in t:
        c += 1
        name = i.split()[0]
        pay = int(i.split()[1])
        if pay < 20000:
            print(name)
        s += pay
    print(f'Средняя зарплата всех {s / c}')
