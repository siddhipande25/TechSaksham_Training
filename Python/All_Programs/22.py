def recursion(n):
    print(n)
    n +=1
    if n <=10:
        return recursion(n)
recursion(1)
    
