a = 'mynameismanasi'
def upper(a):
    s =' '
    for i in a:
        if i != ' ':
            d = (ord(i)-32)
            s = s + (chr(d))
        else:
            s = s + ' '
    print(s)
upper(a)
        
