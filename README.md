cars.py
Program plays with class and subclasses and decorators.
Progam serialize each object for suitable car type to the cars.dat file.
Program unpickling the objects.

Class Vehicles in the file vehicles.py connects subclacces:
 - Vehicles
 - Car
 - Suv
 - Truck

 UML

 --Vehicles--
  - attributes:
    - make
    - model 
    - mileage
    - price

 -methods
    - init(self, make, model, mileage, price):
    - @properties, @setters for each one attribute

--Car--
    - attributes:
        - same as in Vehicles
        - doors
    - methods:
        - same as in vehicles
        - @properties, @setters for doors

--Suv--
    - attributes:
        - same as in Vehicles
        - pas_cap
    - methods:
        - same as in vehicles
        - @properties, @setters for pas_cap

--Truck--
    - attributes:
        - same as in Vehicles
        - drive_type
    - methods:
        - same as in vehicles
        - @properties, @setters for drive_type
