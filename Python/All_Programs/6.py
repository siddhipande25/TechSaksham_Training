n = int(input('Enter number:'))
flag = 0
i = 2

while i < n :
    if n % i == 0:
        i += 1
        flag += 1
        break
if flag == 0:
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')