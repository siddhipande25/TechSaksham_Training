a = int(input('Enter number:'))
tmp = a
sum = 0
while a > 0:
    rem = a % 10
    sum = sum * 10 + rem
    a = a // 10
if tmp == sum :
    print(f'{tmp} is pallindrome')
else:
    print(f'{tmp} is not pallindrome')
    