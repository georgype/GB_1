class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def weight(self):
        kg = int(input("Введите массу асфальта для покрытия одного квадратного метра, кг "))
        cm = int(input("Введите толщину полотна в см "))
        print(self._length * self._width * kg * cm, 'кг')


my_road = Road(20, 5000)
my_road.weight()
