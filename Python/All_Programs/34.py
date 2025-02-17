#Hierarchial inheritance
class A:
    
    def __init__(self,a):
        self.a = a

class B(A):
    pass

class C(A) :
    pass

class D(A):
    def __init__(self, a,b):
       
        super().__init__(a)
        print(f'Addition of two numbers are {self.a + b}')

obj = D(1,2)