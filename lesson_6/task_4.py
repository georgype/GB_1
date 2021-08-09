class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print('Текущая скорость', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Текущая скорость', self.speed)
        if self.speed > 60:
            print('Премышение скорости на', self.speed - 60)


class WorkCar(Car):
    def show_speed(self):
        print('Текущая скорость', self.speed)
        if self.speed > 40:
            print('Премышение скорости на', self.speed - 40)


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


my_car = Car(80, 'green', 'renault', False)
my_car.go()
my_car.stop()
my_car.show_speed()
my_car.turn('направо')

my_town_car = TownCar(75, 'yellow', 'toyota', False)
my_town_car.go()
my_town_car.turn('направо')
my_town_car.show_speed()

my_police_car = PoliceCar(120, 'white', 'bwm')
my_police_car.go()
my_police_car.show_speed()

my_work_car = WorkCar(45, 'black', 'gazelle', False)
my_work_car.show_speed()
my_work_car.stop()

my_sport_car = SportCar(135, 'blue', 'mercedes', True)
my_sport_car.go()
my_sport_car.show_speed()
my_sport_car.turn('налево')