class Four:
    def __init__(self):
        print('i will call first')
    def __del__(self):
        print('i will free space')
    def show(self):
        print('i call')
obj = Four()
obj.show()