#instace method
class First:
    def data(self,name,age):
       self.name = name
       self.age  = age
    def show(self):
        print(f'my name is {self.name} and my age is {self.age}')
obj = First()
obj.data('ram',21)
obj.show()