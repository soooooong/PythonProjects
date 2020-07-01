#coding=utf-8
#!/usr/bin/python3
import random
from  random import randrange 
test = [[0 for i in range(2,5)] for j in range(2,8)]
#print(test)
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 0.9概率是2 0.1概率是4
new_element =  4 if randrange(100) > 89 else 2
#print(new_element)

#初始化二维list
field = [[0 for i in range(4)] for j in range(4)]
print(field)

# 在二维list中随机找一个为位置
all_range =  [(i,j) for i in range(4) for j in range(4) if field[i][j] == 0]
print(all_range)
(i,j) = random.choice([(i,j) for i in range(2) for j in range(3) if field[i][j] == 0])
print((i,j))
