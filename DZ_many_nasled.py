

class Vehicle:
    vehicle_type=None
    def __init__(self):
        pass

class Car:

    def __init__(self, price=1000000, power=200):
        self.price = price
        self.power = power

    def horse_power(self):
        return self.power

class Nissan(Car, Vehicle):

    def __init__(self):
        super().__init__(power=200)
        self.price = 1800000
        self.vehicle_type = 'passenger car'

    def __str__(self):
        return self.__class__.__name__


    def horse_power(self):
        return self.power - 20


nissan = Nissan()
print(nissan.__str__())
print(nissan.vehicle_type, nissan.price)
print(f'price - ', nissan.horse_power())




