#Multiple inheritance

class ClassData:
    def __init__(self,clsname):
        self.clsname = clsname
        print(f'class name {self.clsname}')
class CollegeData:
    def __init__(self,clgname):
        self.clgname = clgname
        print(f'college name {self.clgname}')
class StudentData(ClassData,CollegeData):
    def __init__(self,name,clsname,clgname):
        self.name = name
        print(f'student name {self.name}')
        ClassData.__init__(self,clsname)
        CollegeData.__init__(self,clgname)
obj = StudentData("ABC","XYZ","WIT")
