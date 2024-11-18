class Machine:
    def __init__(self,power) -> None:
        self.power=power
    def power_on(self):
        self.power=True
        print("Power has been turned on")
    def power_off(self):
        self.power=False
        print("Power has been turned off")
class Vehicle(Machine):
    def __init__(self,power,fuel) -> None:
        super().__init__(power)
        self.fuel=fuel
    def start_engine(self):
        print(f"engine started with {self.fuel} type")
    def stop_engine(self):
        print(f"engine stopped with {self.fuel} type")
    def power_on(self):
        self.start_engine()
        super().power_on()
    def power_off(self):
        self.stop_engine()
        super().power_off()
class Electric:
    def charge(self):
        print("charging battery")

class Car(Vehicle,Electric):
    def drive(self):
        print("car is driving")
    def honk(self):
        print("car is honking")
    def autopilot(self):
        print("car is in autopilot mode")
my_vehicle=Vehicle(False,"regular")
my_car=Car(True,"regular")
my_vehicle.power_on()
print(my_vehicle.power)
my_car.power_on()
