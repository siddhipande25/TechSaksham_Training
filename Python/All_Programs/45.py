class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(self.a,self.b)
    def __add__(left,right):
        a = left.a + right.a
        b = left.b + right.b
        return (f"{a,b}")
    def __sub__(left,right):
        a = left.a - right.a
        b = left.b - right.b
        return (f"{a,b}")
    def __mul__(left,right):
        a = left.a * right.a
        b = left.b * right.b
        return (f"{a,b}")
    def __truediv__(left,right):
        a = left.a / right.a
        b = left.b / right.b
        return (f"{a,b}")
obj = A(1,2)
obj1 = A(3,4)
print(obj + obj1)
print(obj * obj1)
print(obj / obj1)
print(obj-obj1)

 
