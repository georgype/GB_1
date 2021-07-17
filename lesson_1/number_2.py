sec = int(input('Введите время в секундах '))
hours = sec // 60 // 60
minutes = sec // 60 % 60
seconds = sec % 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
