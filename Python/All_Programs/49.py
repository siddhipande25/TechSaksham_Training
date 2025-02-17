name = input('Enter file name which you want to create:')
f = open(f"D:\TY\\{name}.txt","a")
f.write("hello")
f.close()