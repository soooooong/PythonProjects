__author__ = 'song'
#提前定义属性
class Student(object):
    def __init__(self,name,score):
        self.name = name  #添加属性name 将实例时传的参数赋值给实例化后self对应的属性name
        self.score = score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

#student中有__init__方法，实例时传入的参数得与__init__方法的参数匹配，self不需要传
bar=Student('song',99) #bar对应self song对应name 99对应score
print(bar.name,bar.score)
bar.print_score()

#不提前定义属性,实例化之后添加属性
class Student_no(object):
    pass

bart = Student_no()
bart.name='song_'
print(bart.name)



