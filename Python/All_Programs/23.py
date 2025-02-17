def recursion(n):
    def table(n1):
        print(n*n1)
        n1 +=1
        if n1 <=10:
            return table(n1)
    table(1)
    n += 1
    if n <=10:
        return recursion(n) 
recursion(1)
