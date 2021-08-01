with open('text_task_2.txt', 'r') as t:
    n_str = 0
    for i in t:
        n_str += 1
        print(f'Слов в {n_str}-й строке {len(i.split())}')
    print(f'Количество строк {n_str}')