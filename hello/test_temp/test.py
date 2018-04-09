__author__ = 'song'
class Student(object):
    def __init__(self,name):
        self.name=name
    pass

def say_hello(self):
    print('hello')

s1=Student('s1')
print(s1.name)

Student.say_hello=say_hello
s1.say_hello()


