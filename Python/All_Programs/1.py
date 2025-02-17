a=[88,34,1,2,2,1,85,77,89]
b = set(a)
n = 9
lowest = a[0]
slowest= -1
for i in range(n):
    if b[i] < lowest:
        slowest = lowest
        lowest = b[i]
    if b[i] > slowest and b[i] < lowest:
        slowest = b[i]
print(slowest,lowest)