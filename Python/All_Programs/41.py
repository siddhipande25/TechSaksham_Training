class A:
    def __show(self):
        print('private')
    
    def call(self):
        print('call another method')
        self.__show()

obj = A()
obj.call()
