my_str = input('Введите строку ').split()
for i in range(len(my_str)):
    print(i + 1, my_str[i][:10])