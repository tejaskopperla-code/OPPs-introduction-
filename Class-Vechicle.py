class Vechicles:

    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vechicles):
    pass


School_Bus = Bus("School Volvo",100,12)
print("Vechicle name", School_Bus.name," Speed ",School_Bus.max_speed,"Mileage", School_Bus.mileage)