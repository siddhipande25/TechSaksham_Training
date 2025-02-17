def len(a):
    c = 0
    while a > 0:
        rem = a % 10
        c += 1
        a = a // 10
    return c
length = len(56)
print(f'The length of {a} is {length}')
