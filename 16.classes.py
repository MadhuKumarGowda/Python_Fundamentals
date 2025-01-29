# Classes are blueprint of objects 
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def moves(self):        
        print(f"Moves along with make of {self.make} and model {self.model}")
        
    def get_Make_Model(self):
        print(f"I'm a {self.make} {self.model}")

mycar = Vehicle("Hyundai","Verna")
# print("Make of my car is:", mycar.make)
# print(f"Model of my car is: {mycar.model}")
mycar.get_Make_Model()
mycar.moves()

newCar =  Vehicle("Ford","Mustang")
newCar.get_Make_Model()
newCar.moves()

class AeroPlane(Vehicle):
    def __init__(self, make, model,faa_id):
        # Super with parameter will inherit the values of make and model form parent class
        super().__init__(make, model)
        self.faa_id = faa_id
        
    def moves(self):
        print(f"Flies along... with {self.faa_id}")

class Truck(Vehicle):
    def moves(self):
        print("Rumble along...")

# Pass is the keyword to inherit all props and methods as it from parent class
class GolfCart(Vehicle):
    pass

aeroPlane = AeroPlane("Emirates", "A380", "EK214")
truck = Truck("AL","Truck001")
golfwagon = GolfCart("Golf","GC0001")

aeroPlane.get_Make_Model()
aeroPlane.moves()

truck.get_Make_Model()
truck.moves()

golfwagon.get_Make_Model()
golfwagon.moves()

# Polymorphism is same method return different set of responses
print("Polymorphism".center(100,"*"))

for v in (mycar, newCar, aeroPlane, truck, golfwagon):
    v.get_Make_Model()
    v.moves()