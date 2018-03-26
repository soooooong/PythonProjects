import os
import sys
print("命令行参数：")
for i in sys.argv:
    print(i)
import book_example  #引用同一文件夹得模块可以直接引用
#导入book_example模块时会执行一遍

sys.path.append("..") #为了引用上层文件夹下的 helloworld.hello 模块

import helloworld.hello
helloworld.hello.printhello()

from helloworld.hello import printhello
printhello()

from helloworld import hello
hello.printhello()

print(sys.path)