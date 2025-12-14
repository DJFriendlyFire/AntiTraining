class Car:
    def __init__(self, make: str, model: str, year: int, mileage: int):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance

    def get_info(self):
        return f'{self.make} {self.model} {self.year}, Mileage: {self.mileage}'


car = Car('Ford', 'Mustang', 2000, 5000)
car.drive(100)
print(car.get_info())