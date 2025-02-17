#Hybrid method

class Student1:
    def show1(self):
        print('I am student 1')

class Student2(Student1):
    def show2(self):
        print('I am student 2')

class Student3:
    def show3(self):
        print('I am student 3')      

class Teacher(Student2,Student3):
    def show4(self):
        print('I am a teacher of student 1 and student 2 and student 3')
obj = Teacher()
obj.show1()
obj.show2()
obj.show3()
obj.show4()