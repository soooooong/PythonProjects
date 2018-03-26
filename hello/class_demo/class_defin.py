__author__ = 'song'


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



