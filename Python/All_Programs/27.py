#class method
class Second:
    @classmethod
    def show(cls,name,age):
        cls.name = name
        cls.age = age
        print(f'my name is {cls.name} and my age is {cls.age}')
Second.show('mina',57)
