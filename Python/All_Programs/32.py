class Parent:
    
    def __init__(self,house):
        self.house = house
    
        
class Child(Parent):
    def cshow(self):
        print(f'My father gifted me {self.car}')
obj = Child('dreamhouse','bmw')
obj.cshow()