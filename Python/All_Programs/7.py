l=[]
for n in range(2, 101):  # Loop from 1 to 100
    flag = 0
    i = 2
    while i < n:
        if n % i == 0:
            flag += 1
            break
        i += 1
    if flag == 0 :
        l.append(n)
print(l) 
         
