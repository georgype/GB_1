with open('text_task_4.txt') as t, open('result_task_4.txt', 'w') as f:
    d = {'One': 'один',
         'Two': 'два',
         'Three': 'три',
         'Four': 'четыре'}
    for i in t:
        f.write(f'{d.get(i.split()[0])} {" ".join(i.split()[1:])}\n')