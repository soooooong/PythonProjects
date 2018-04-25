__author__ = 'song'
###############################################################
#tuple原本表示不变的集合，namedtuple,用来创建一个自定义的tuple对象，规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
#新对象它具备tuple的不变性，又可以根据属性来引用

from collections import  namedtuple
point =namedtuple('point',['x','y'])#定义为点
p=point(1,2)
print(p.x)
print(p.y)

circle = namedtuple('circle',['x','y','r'])
circle1=circle(1,2,5)
print(circle1.r)#定义一个圆

#双向链表
#deque
from collections import deque
q=deque(['a','b','c'])
q.append('x') #尾部添加
q.appendleft('y')#头部添加
print(q)

q1=q.pop()
print(q1)#尾部取
q2=q.popleft()
print(q2)#头部取
###############################################################
#dict是无序的，OrderedDict可以按照dict元素添加的顺序排序dict，就可以实现一个FIFO（先进先出）的dict

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

order1=LastUpdatedOrderedDict(3)
order1.__setitem__('name','song')
order1.__setitem__('age','12')
order1.__setitem__('school','T')
order1.__setitem__('test','s') #会移除一个元素

#计数器
from collections import  Counter
c=Counter()
str1='programer'
for ch in str1: #统计字符串中各字符出现次数
    c[ch]=c[ch]+1
print(c)

###############################################################
#struct 解决bytes和其他二进制数据类型的转换
#b'str'可以表示字节  例：b'\x00\x9c@c'

#@contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
#结果，先执行函数tag yield之前内容，再执行with中，再执行yield之后
#<h1>
#hello
#world
#</h1>





