with open('text_task_1.txt', 'w') as t:
    a = input()
    while a:
        t.write(a+'\n')
        a = input()