# carsData.py
'''
Make use sbclasses.
'''
import vehicles
import pickle
import os
from pathlib import Path

def main():
    # direction for saving dictionary
    os.chdir(Path.cwd()/Path('Cars'))
    
    # creating Car object
    car = vehicles.Car('Volvo', 'V5', 123, 1234.56, 5)
    suv = vehicles.Suv('Toyota','Ty234',234,2341.23,6)
    truck = vehicles.Truck('Jeep','Jp34',567,786.54,4)
    
    cars = {'car1':car, 'suv1':suv, 'truck1': truck }
    
    # pickle the object
    save(cars)
    print('Object is pickled!\n')
    
    # unpickling objects from the file.dat
    data = load()
    
    for car, object in data.items():
        print(f"This is {car}: ")
        print(f"make:{object.make}")
        print(f"model:{object.model}")
        print(f"mileage:{object.mileage}")
        print(f"price:{object.price}")

        try:
            print(f"doors:{object.doors}")
        except AttributeError:
            pass
        try:
            print(f"passenger capicity: {object.pass_cap}")
        except AttributeError:
            pass
        try:
            print(f"drive type:{object.drive_type}")
        except AttributeError:
            pass
        print()
    
    

def save(objects):
    outputFile = open('cars.dat','wb')
    pickle.dump(objects, outputFile)
    outputFile.close()
    
def load():
    inputFile = open('cars.dat','rb')
    return pickle.load(inputFile)  
    
    


main()
