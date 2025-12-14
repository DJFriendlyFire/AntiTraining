from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, salary: float, position=None):
        self.name = name
        self.salary = salary
        self.position = position

    def get_info(self):
        return f'{self.name}, {self.position}, {self.salary}'

    @abstractmethod
    def calculate_bonus(self):
        pass


class Developer(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)
        self.position = 'Developer'

    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)
        self.position = 'Manager'

    def calculate_bonus(self):
        return self.salary * 0.15


dev = Developer('Alice', 60000)
mng = Manager('Bob', 80000)

print(dev.get_info())
print(mng.get_info())

print(dev.calculate_bonus())
print(mng.calculate_bonus())
