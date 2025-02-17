class A:
   def __init__(self,__amt):
      self.__amt = __amt
   def show1(self):
      print(self.__amt)

class B(A):
   def show(self):
      print(self.__amt)

obj = B(10)
obj.show()
#if we try to acces private variable by child method then we cat't access it

#  But at the same time if we try to access it by parent method then we can access it
      
  