class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Пишем ручкой")


class Pencil(Stationery):
    def draw(self):
        print('Пишем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Пишем маркером')


my_pen = Pen('Синяя ручка')
my_pen.draw()

my_pencil = Pencil('Тонкий карандаш')
my_pencil.draw()

my_handle = Handle('Маркер Маши')
my_handle.draw()