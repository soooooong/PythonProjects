#!/usr/bin/python3
#coding=utf-8
#curses 用来在终端上显示图形界面
import curses

#random 生成随机数
from random import randrange,choice

# collections 提供一个字典的子类，defaultdict 可以指定key 值不存在时，value的默认值
from collections import defaultdict

#所有有效的行为
actions = ['up','left','down','Right','restart','exit']

#ord 获取ascii
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

#zip 将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组
#将wasdr和上下左右关联
#>>>a = [1,2,3]
#>>> b = [4,5,6]
#>>> c = [4,5,6,7,8]
#>>> list(zipped)  # list() 转换为列表
#[(1, 4), (2, 5), (3, 6)]

#dict 字典
actions_dict = dict(list(zip(letter_codes,actions*2)))
print(actions_dict)

class GameField(object):
    def __init__(self,height = 4,width = 4,win = 2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()
        print('__init__')

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()
    def spawn(self):
#以0.1的概率生成4，以0.9概率生成2
        new_element =  4 if randrange(100) > 89 else 2
#choice() 方法返回一个列表，元组或字符串的随机项。
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
#将生成的2或4放到2维list中
        self.field[i][j] = new_element
    def draw(self,screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'


def main(stdscr):
    def init():
        game_field.reset()
        return 'game'
    def game():
        #画出当前棋盘
        game_field.draw(stdscr)

    state_actions  = {
        'init' : init,
        'game': game,
    }


    
    # 设置win的状态最大数值为 32
    game_field = GameField(win=32)

    state = 'init'

    while state != 'exit':
        state = state_actions[state]()
    

# curses 库为基于文本的终端提供独立于终端的屏幕绘制和键盘处理
# curses.wrapper 接受一个可调用对象，可调用的对象在try中被调用，可以捕获异常
# main 的参数  stdscr是一个整个屏幕的窗口对象
curses.wrapper(main)