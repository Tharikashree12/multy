class car:
    def __init__(self, speed, fuel_level):
        self.__speed = speed
        self.__fuel_level = fuel_level
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        if 0 <= speed <= speed:
            self.__speed = speed
        else:
            print("Invalid speed")
        def show_efficiency(self):
            print(f"Fuel Efficiency: {self.__fuel_efficiency()}km/1")
car1 = car(100, 50)
car1.show_efficiency()
car1.set_speed()
car1.show_efficiency()
car1.set_speed()
print("Fuel Level:", car1.__fuel_level)
