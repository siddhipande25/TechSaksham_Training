f = open("D:\hello\\f.txt","r")
a = f.readlines()
c = 0
for i in a:
    c += 1
print(f'Total lines in files are {c}')
f.close()
