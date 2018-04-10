__author__ = 'song'
import  sys
#提前定义属性
class Student(object):
    def __init__(self,name,score):
        self.name = name  #添加属性name 将实例时传的参数赋值给实例化后self对应的属性name
        self.score = score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

#student中有__init__方法，实例时传入的参数得与__init__方法的参数匹配，self不需要传
student=Student('old',99) #bar对应self song对应name 99对应score
print(student.name,':',student.score)
student.print_score()



###############################################################
#不提前定义属性,实例化之后添加属性
class Student_no_attribute (object):
    pass

bart = Student_no_attribute()
bart.name='old'
print(bart.name)


###############################################################
#私有属性
class student_private_sttribute(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def  get_name(self):
        return self.__name
    def get_score(self):
        return  self.__score

student_private_sttribute=student_private_sttribute('song',78)
print(student_private_sttribute.get_name())
print(student_private_sttribute.get_score())


###############################################################
#多态
class animal(object):
    def run(self):
        print('animal is running ...')
class dog(animal):
    def run(self):
        print('dog is running')
class cat(animal):
    def run(self):
        print('car is runing')

def run_inheritance(animal):
    animal.run()

dog=dog()
dog.run()
cat=cat()
cat.run()

run_inheritance(dog)

###############################################################
#获取信息
#判断一个类是否有某个属性或函数
print(hasattr(bart,'name'))
#获取属性
print(getattr(student,'score'))
print(hasattr(dog,'run'))

#获取类型
print(type(dog))
print(type(12)==type(67))
#判断是否是函数
import  types
print(type(run_inheritance)== types.FunctionType)

#判断class类型     isinstance()
print(isinstance(dog,animal))
print(isinstance(123,int))

#获得对象的所有属性和方法 dir()
print(dir(dog))


###############################################################
#类属性
class student_class_inheritance(object):
    name = 'student'

s1=student_class_inheritance()
print(s1.name, 'line::',sys._getframe().f_lineno)
s2=student_class_inheritance()
print(s2.name,'line::',sys._getframe().f_lineno)

###############################################################
###############################################################
#动态绑定类方法
#例1
class student_dynamic_fun(object):
    def __init__(self,name):
        self.name=name

#先定义实例s1 s2 再绑定类方法，实例也可以拿到方法
s1=student_dynamic_fun("t1")
s2=student_dynamic_fun('t2')

def set_student_name(self,name):
    self.name=name
student_dynamic_fun.set_name = set_student_name

s1.set_name('s1')
s2.set_name("s2")
print(s1.name,s2.name)

#例2
__author__ = 'song'
class student_dynamic_fun1(object):
    def __init__(self,name):
        self.name=name
    pass

def say_hello(self):
    print('hello')

s1=student_dynamic_fun1('s1')
print(s1.name)

student_dynamic_fun1.say_hello=say_hello
s1.say_hello()
###############################################################
#限制类属性
class student_limit_sttribute(object):
    __slots__ = ('name','age')

s1=student_limit_sttribute()
#添加score属性会报错
#s1.score=12


###############################################################
#装饰器应用 @property

#检查设置值
class student_property(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score is not integer')
        if(value > 100 or value < 0):
            raise ValueError('must butween 0-100')
        self.score=value
s3=student_property()

#给score赋值1000就会报错
#s3.score=1000
#设置只读属性,不定义setter方法就会是只读
class student_sttribute_only_read(object):
    @property
    def birth(self):
        return self.__name
#    @birth.setter
#    def


#s3=student_sttribute_only_read()
#s3.birth=30

###############################################################
#__slots __
#子类如果也定义__slots__可以使用父类__slots__定义的属性
class Student_slots_father(object):
    __slots__=("name")
class Student_slots_son(Student_slots_father):
    __slots__=("age")

Student1=Student_slots_father()
Student2=Student_slots_son()
Student1.name='s1_184'
print(Student1.name)
#Student1.age=12  #__slots__没有设置age属性，设置就会报错
Student2.name='s2_187'
print(Student2.name)
Student2.age=12
print(Student2.age)


###############################################################
#__getattr__实例的类中没有调用的属性或方法时，如有实现__getattr__，则调用__getattr__方法
class adaptee(object):
    def foo(self):
        print('foo in adaptee')
    def bar(self):
        print('bar in adaptee')

class adapter(object):
    def __init__(self):
        self.adaptee = adaptee()

    def foo(self):
        print('foo in adapter')
        self.adaptee.foo()

    def __getattr__(self, name):
        return getattr(self.adaptee, name)

a = adapter()
a.foo()
a.bar()
###############################################################
#错误处理
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
###############################################################
#类实例化为json
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

print(json.dumps(s, default=lambda obj: obj.__dict__))






























