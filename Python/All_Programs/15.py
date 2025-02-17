name = input('enter your name:')
print(f'Welcome to our restaurant {name}')
food = { 'veg':['panner240','panner_tika240'],
        'non_veg':['biryani','eggs']

       }
sfood = input('Enter your choice:')
c = 0
for i in food[sfood]:
    print(f'{i} to order press {c}')
    c += 1
order =int(input('enter value to order food:'))
print('your order is placed')
print(food[sfood],order)