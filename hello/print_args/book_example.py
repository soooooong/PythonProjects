__author__ = 'song'
import  sys
def printtest():
    print(__name__)
print(__name__)
print(__file__)

#不能给字符串某个位置单独赋值，拼接或重新赋值
st="Hello world"
st = st[:6]+"Python"
print(st)


#字符串格式化
charA =65
print("ascii 码65代表： %c" % charA)

num1 = 0xEF3
num2 = 0xAB03
print("转换成十进制分别为 %u和 %u" % (num1,num2))
#辅助符号 * - + 等，例：位置 在 %u的%与u之间
num=234.567890
print("%.2f" % num)

#列表操作
list = [123,'abc',4.56,['inner','list'],7-9j]

print(list[0])
print(list[1:4])
print(list[:3])
print(list[3][1])

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

#for in
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print(fruits[index],'line::',sys._getframe().f_lineno)

#列表生成式
l=[x * x for x in range(1, 11)]
print(l)



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