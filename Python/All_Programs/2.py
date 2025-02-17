name=input('enter name:')
mother_name=input('enter mother name:')
def result():
    a= 39
    b= 59
    c = 76
    avg = (a+b+c)//3
    print(f'the average is {avg}')
    print(f'marks of physics,chemistry,bio are {a},{b},{c}')
    

if name=='ram' and mother_name=='rina':
   result()
   
else:
    print('invalid credentials')
