def person(**kwargs):
    print(*kwargs.values())


person(name=input('Введите имя '),
       surname=input('Введите фамилию '),
       birth=input('Введите дату рождения '),
       city=input('Введите город '),
       email=input('Введите email '),
       phone=input('Введите номер телефона ')
       )
