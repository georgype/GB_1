with open('text_task_5.txt', 'w') as t:
    i = input('Для окончания ввода оставте строку пустой ')
    a = []
    while i:
        a.append(i)
        i = input('Для окончания ввода оставте строку пустой ')
    t.write(' '.join(a))
with open('text_task_5.txt') as t:
    print(f'Сумма элементов = {sum([int(i) for i in t.read().split()])}')