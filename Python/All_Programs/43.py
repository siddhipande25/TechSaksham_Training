class A:
    def show(self):
        print('first')

class B(A):
    def show(self):
        print('second')

obj = B()
obj.show()