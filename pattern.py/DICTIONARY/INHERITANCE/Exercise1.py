class vehicle:
    def greet_vehicle(self):
        print("brand: audi")
class car(vehicle):
    def greet_car(self):
        print("model: pept")
class sportscar(car):
    def greet_sportscar(self):
        print("speed: 80 km/h")
m = sportscar()
m.greet_vehicle()
m.greet_car()
m.greet_sportscar()

