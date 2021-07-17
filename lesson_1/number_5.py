earn = int(input('Введите выручку '))
cost = int(input('Введите издержки '))
profit = earn - cost
if profit > 0:
    print(f'Прибыль {profit}')
    print(f"Рентбельность {profit / earn:.2%}")
    num = int(input('Введите количество сотрудников '))
    print(f'Прибыль в фирме на одного сотрудника {profit / num:.2f}')
else:
    print('Убыток')
