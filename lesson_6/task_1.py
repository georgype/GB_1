from time import sleep


class TrafficLight:
    __color = 'red'

    def running(self):
        for i in range(7):
            print(self.__color)
            sleep(1)
        self.__color = 'yellow'
        for i in range(2):
            print(self.__color)
            sleep(1)
        self.__color = 'green'
        for i in range(5):
            print(self.__color)
            sleep(1)


My_traffic = TrafficLight()
My_traffic.running()
