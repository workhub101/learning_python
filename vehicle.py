class Vehicle:
    def __init__(self,name,model) -> None:
        self.name= name
        self.model=model
    def engine_start(self):
        print(f"{self.name} {self.model} engine started")
    def engine_stop(self):
        print(f"{self.name} {self.model} engine stopped")
class Car(Vehicle):
    def drive(self):
        print(f"The {self.model} {self.name} is driving")
    def honk(self):
        print(f"The {self.model} {self.name} is honking")
class Bike(Vehicle):
    def ride(self):
        print(f"{self.name} is riding")

my_car=Car("Car","2018")
my_bike=Bike("Bike","2024")
my_car.engine_start()
my_car.engine_stop()
my_car.honk()
my_car.drive()
my_bike.engine_start()
my_bike.engine_stop()
my_bike.ride()
