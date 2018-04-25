__author__ = 'song'

###############################################################
#迭代器 itertools

#无限迭代器
import itertools
natuals = itertools.count(1)
#for i in natuals:
#    print(i) #会打印出自然数序列，不会停止

#cycle()会把传入的一个序列无限重复
cs = itertools.cycle('abc')
#for c in cs:
#    print(c)  #不停循环打印a,b,c,a,b,b

#cycle()会把传入的一个序列无限重复，提供第二个参数可以限定重复次数
ns=itertools.repeat('a',3)
for n in ns:
    print(n)
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代
for c in itertools.chain('123', 'abs'):
    print(c)
#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key ,group in itertools.groupby('AAABBBCCA'):
    print(key,list(group))
    #也可以自定义规则，比如可以忽略大小写分组
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    #upper()将小写字母转化为大写
    print(key, list(group))
