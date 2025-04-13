#Assignment 1: Design Your Own Class

class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model, camera_resolution):
        super().__init__(brand, model)
        self.camera_resolution = camera_resolution

    def display_info(self):
        super().display_info()
        print(f"Camera Resolution: {self.camera_resolution}MP")

phone = FlagshipPhone("Samsung", "S22", 50)
phone.display_info()


#Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

vehicles = [Car(), Plane()]
for vehicle in vehicles:
    vehicle.move()