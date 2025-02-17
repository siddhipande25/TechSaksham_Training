n= int(input('Enter number:'))
tmp = n
arm = 0
order = len(str(n))
while n > 0:
    rem = n % 10
    arm += rem ** order
    n = n// 10
if tmp == arm:
    print(f'{tmp} is armstrong number')
else:
    print(f'{tmp} is not armstrong number')