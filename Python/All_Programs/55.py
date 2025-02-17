f = open("D:\hello\\f.txt","r")
a = f.readlines()
dummy =input('enter word you want to search:')
for i in a:
    a1 = i.split()
    for j in a1:
        if j.lower() == dummy:
            print('found')
            break
else:
    print('Not found')
   
    