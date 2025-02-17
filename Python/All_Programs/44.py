class First:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(self.a,self.b)
obj = First(1,2)
obj1 = First(3,4)
obj2 = First(obj.a * obj1.a,obj.b * obj1.b)
