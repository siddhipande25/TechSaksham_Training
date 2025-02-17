class A:
   def __init__(self,_amt):
      self._amt = _amt
   def show1(self):
      print(self._amt)

class B(A):
   def show(self):
      print(self._amt)

obj = B(10)
obj.show()


# we can access protected variable in inherited class