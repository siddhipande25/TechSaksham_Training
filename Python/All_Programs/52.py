f = open("D:\hello\\f.txt","r")
a = f.readlines()
c = 0
for i in range(len(a)):
    c += len(a[i])
print(f'Total words in files are {c}')
f.close()
