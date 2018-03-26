__author__ = 'song'
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
