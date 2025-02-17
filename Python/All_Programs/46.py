from abc import ABC,abstractmethod
class Data(ABC):
    @abstractmethod
    def show(self):
        pass
class Data1(Data):
    def show(self):
        print('Abstraction')

obj = Data1()

obj.show()