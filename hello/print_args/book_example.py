__author__ = 'song'
import  sys
from collections import Iterable
from collections import Iterator
from functools import reduce

def printtest():
    print(__name__)
print(__name__)
print(__file__)
###############################################################
#不能给字符串某个位置单独赋值，拼接或重新赋值
st="Hello world"
st = st[:6]+"Python"
print(st)

###############################################################
#字符串格式化
charA =65
print("ascii 码65代表： %c" % charA)

num1 = 0xEF3
num2 = 0xAB03
print("转换成十进制分别为 %u和 %u" % (num1,num2))
#辅助符号 * - + 等，例：位置 在 %u的%与u之间
num=234.567890
print("%.2f" % num)

###############################################################
#列表操作
list1 = [123,'abc',4.56,['inner','list1'],7-9j]

print(list1[0])
print(list1[1:4])
print(list1[:3])
print(list1[3][1])
###############################################################
#字典
ab = { 'sw':'roop.com',
       'rry':'wall.com',
        'moto':'lang.com',
        'spa':'hot.com',
}
print(ab)
#删除
del ab['spa']
print(ab)
#添加
ab['add_1']='add_val'
if 'add_1' in ab:
    print(ab['add_1'])
###############################################################
#for in
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print(fruits[index],'line::',sys._getframe().f_lineno)
###############################################################
#列表生成式
l=[x * x for x in range(1, 11)]
print(l)

def f(x):
    return x*x
#append()给列表里添加元素
L=[]
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print('line:',sys._getframe().f_lineno,L)

###############################################################
#生成器
#斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 有 关键字 yield 这个函数就不再是一个普通函数，而是一个generator
#变成generator的函数，遇到yield语句返回，再次调用next()的时候执行，再次执行时从上次返回的yield语句处继续执行
#用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break



###############################################################
#with  open as
#with open('abc.txt','r') as f:
#balabalabala
#等价于
#try:
#f = open('abc.txt','r')
#except:
#pass
#else:
#balabalabala
#finally:
#f.close()
###############################################################
#生成器注意点：生成器只能迭代一遍
def get_province_population(filename):
    with open(filename) as f:
        for line in f:
            yield int(line)
gen=get_province_population('population.txt')
#while 遍历过一遍， sum遍历时就没有了
#1
while True:
    try:
        x = next(gen)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
#2 屏蔽掉#1，以下sum结果会正确，因为#1已经迭代过一遍
all_populaton = sum(gen)
print(all_populaton)

#生成器重新赋值可以再次使用
gen=get_province_population('population.txt')
all_populaton = sum(gen)
print(all_populaton)

###############################################################
#map() and reduce()
#map() 使用list函数将iterator 转化为list
def square(x):
    return x ** 2 *x #三次方
L=[1,2,3,4,5]
gen=map(square,L )
print('line:',sys._getframe().f_lineno, '  ',isinstance(gen, Iterable),isinstance(gen, Iterator))
print(list(gen))

#reduce()
def fn(x, y):
    return x + y

print(reduce(fn, [1, 3, 5, 7, 9]))

#pyhton版本
print(sys.version)

#结合map() and reduce()
#map()返回一个itrator，再交给reduce处理
#1
def str2num(s):
    bas={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    return bas[s]
str=map(str2num,'14590')
#2
def fn(x,y):
    return 10 * x+y
num3=reduce(fn,str)
print(num3)

###############################################################
#闭包  厉害
#例：实现1
#定义两条线，输入x输出y
def line_conf(a,b):
    def line(x):
        return a*x+b
    return  line
line1=line_conf(2,3)
line2=line_conf(5,6)

y1=line1(100)
y2=line2(100)
print('method1:')
print('line1: x1= 100  y1=', y1)
print('line2  x2= 100  y2=' ,y2)

#实现2
print('method2:')
def line_conf(a,b):
    return  lambda x:a*x+b
line1=line_conf(2,3)
line2=line_conf(5,6)

y1=line1(100)
y2=line2(100)
print('line1: x1= 100  y1=', y1)
print('line2  x2= 100  y2=' ,y2)

###############################################################
#filter
#删除返回false项
#取偶数
def is_even(n):
#    print (not(n%2==1))
    return  (not n%2)
print(list(filter(is_even, [1, 2, 4, 5, 6, 9, 10, 15])))

#应用
#取素数
def main():
    for n in primes():
        if n < 10:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
main()

###############################################################
#sorted()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
for i in L:
    print(i[0])

#一个一个获取名字 按名字排序
def get_onename(i):
    return i[0]
#for i in L:
#    print(get_onename(i))
print(sorted(L,key=get_onename))

###############################################################
#带参数的装饰器
import logging
F = True          #step 1 装饰器的开关变量
def outer(flag):  #step 2
    def wrapper(func): #step 4
        def inner(*args,**kwargs): #stpe 6
            if flag:               #step 9
                print('before')   #step 10
                ret = func(*args,**kwargs)  #step 11  执行原函数
                print('fun.__name %s'% func.__name__)
                print('after')             #step13
            else:
                ret = func(*args,**kwargs)
                print('fun.__name %s'% func.__name__)
            return ret                     #step 14
        return inner    #step 7
    return wrapper     #step 5

@outer(F)   #先执行step 3 ：outer(True)这个函数，然后step 6：@wrapper   #此处把开关参数传递给装饰器函数
def hahaha():
    print('hahaha')  #step 12
    logging.warn('warning')     #warning 执行位置不确定
hahaha()    # step 8    相当于inner()


#类装饰器
class Foo(object):
    def __init__(self,func):
        self.__func=func
    def __call__(self, *args, **kwargs):
        print('class decorator runing')
        self.__func()
        print('class decorator enging')
@Foo
def bar():
    print("bar")
bar()

#需要使用@functools.wraps
#使用@functools.wraps传入原函数的元信息
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):  #注意参数
            print('%s %s():' % (text, func.__name__))
            print(" %s step 3" % text)
            return func(*args, **kw)
        print(" %s step 2" % text)
        return wrapper
    print(" %s step 1" % text)
    return decorator

@log('execute')
def now():
    print('2018-4-3')
now()