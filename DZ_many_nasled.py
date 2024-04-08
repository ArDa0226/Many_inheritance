

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


    def horse_power(self):
        return f'{self.__class__.__name__} has {self.power - 20} horse power,'


nissan = Nissan()
print('Price -', nissan.price, '$', nissan.horse_power(), nissan.vehicle_type)




