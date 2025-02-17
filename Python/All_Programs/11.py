def abc():
    yield 12 
    yield 13
a=abc()
print(next(a))
print(next(a))