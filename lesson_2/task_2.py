a = input('Введите элемент массива (для завершения ввода оставте строку пустой) ')
my_list =[]
while a:
    my_list.append(a)
    a = input('Введите элемент массива (для завершения ввода оставте строку пустой) ')
for i in range(1, len(my_list), 2):
    my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
print(my_list)