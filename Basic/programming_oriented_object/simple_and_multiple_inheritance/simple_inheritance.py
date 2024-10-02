class Vehicle:
    def __init__(self, color, license_plate, number_of_wheels):
        self.color = color
        self.license_plate = license_plate
        self.number_of_wheels = number_of_wheels

    def start_engine(self):
        print("Starting the engine")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


class Motorcycle(Vehicle):
    pass


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def __init__(self, color, license_plate, number_of_wheels, loaded):
        super().__init__(color, license_plate, number_of_wheels)
        self.loaded = loaded

    def is_loaded(self):
        print(f"{'Yes' if self.loaded else 'No'} I'm loaded")


motorcycle = Motorcycle("black", "abc-1234", 2)
car = Car("white", "xde-0098", 4)
truck = Truck("purple", "gfd-8712", 8, True)

print(motorcycle)
print(car)
print(truck)
