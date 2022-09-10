# vehicles.py
'''
Refer to the README.md
'''


class Vehicles:
    '''Super class for subclasse'''

    def __init__(self, make, model, mileage, price):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price

        #
        # getters
        #
        #
        @property
        def maKe(self):
            return self.make

        @property
        def moDel(self):
            return self.model

        @property
        def mileaGe(self):
            return self.mileage

        @property
        def priCe(self):
            return self.price

        #
        #
        # setters
        #
        @maKe.setter
        def maKe(self, make):
            self.make = make

        @moDel.setter
        def moDel(self, model):
            self.model = model

        @mileaGe.setter
        def mileaGe(self, mileage):
            self.mileage = mileage

        @priCe.setter
        def priCe(self, price):
            self.price = price

#
#
# creating subclass Car, which iherits from Vehicles
#


class Car(Vehicles):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)

        self.doors = doors

        @property
        def dooRs(self):
            return self.doors

        @dooRs.setter
        def dooRs(self, doors):
            self.doors = doors

#
#
# creating subclass Suv
#


class Suv(Vehicles):
    def __init__(self, make, model, mileage, price, pass_cap):
        super().__init__(make, model, mileage, price)
        self.pass_cap = pass_cap

        @property
        def passCap(self):
            return self.pass_cap

        @passCap.setter
        def passCap(self, pass_cap):
            self.pass_cap = pass_cap


class Truck(Vehicles):
    def __init__(self, make, model, mileage, price, drive_type):
        super().__init__(make, model, mileage, price)
        self.drive_type = drive_type

        @property
        def driveType(self):
            return self.drive_type

        @driveType.setter
        def driveType(self, drive_type):
            self.drive_type = drive_type
