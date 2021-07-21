my_rate = [7, 5, 3, 3, 2]
print(my_rate)
a = int(input('Введите новый элемент рейтинга '))
while a:
    for i in range(len(my_rate)):
        if a > my_rate[i]:
            my_rate.insert(i, a)
            print(my_rate)
            break
    else:
        my_rate.append(a)
        print(my_rate)
    a = int(input('Введите новый элемент рейтинга (для завершения введите "0") '))
