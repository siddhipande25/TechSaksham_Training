class A:
   def __init__(self,__amt):
      self.__amt = __amt
  
obj = A(23)
print(obj._A__amt)
# we can access private variable outside class using class name