a = 'bvbvbsvb'
def upper(a):
    s =' '
    for i in a: 
        d = (ord(i)-32)
        s = s + (chr(d))
    print(s)
upper(a)