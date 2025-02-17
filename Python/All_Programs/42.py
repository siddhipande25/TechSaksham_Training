class A:
    def __show():
        print('private method calling outside ')
    __show() #call private method without passing instance 
       

obj = A()
# obj._A__show()

