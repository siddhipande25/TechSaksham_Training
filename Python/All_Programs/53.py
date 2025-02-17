f = open("D:\hello\\f.txt","r")
a = f.readlines()
c1 = 0
c2 = 0
for i in a:
    for j in a:
        if j == " ":
            c1 += 1
        else:
            c2 +=1
print(c1,c2)