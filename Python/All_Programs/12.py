row = 1
while row <= 4:
    cols = 1
    while cols <= 4 - row:  
        print(' ', end=' ')
        cols += 1

    col = 1
    while col < (2 * row): 
        print(chr(96 + row ), end=' ')
        col += 1

    print()  
    row += 1 
