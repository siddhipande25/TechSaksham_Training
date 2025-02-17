#private
class Data:
    def __init__(self,__amt):
        self.__amt = __amt
        print(self.__amt)
obj = Data(12)



#protected
class Data1:
    def __init__(self,_amt):
        self.__amt = _amt
        print(self._amt)
obj = Data("hedb")
obj.__amt = 'snn'
print(obj.__amt)

#public
class Data2:
    def __init__(self,amt):
        self.amt = amt
        print(self.amt)
obj = Data("hedb")
obj.amt = 'sffs'
print(obj.amt)

