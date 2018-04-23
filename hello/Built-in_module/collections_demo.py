__author__ = 'song'
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



