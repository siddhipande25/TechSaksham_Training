import os
file=input('Enter file name which you want to delete:')
if os.path.exists(file):
    os.remove(file)
else:
    print('File not found')
    