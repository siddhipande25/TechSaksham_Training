a = [3, 1, 4, 1, 5, 9]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] >= a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
