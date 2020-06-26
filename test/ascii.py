from PIL import Image
import argparse #是一个用来解析命令行参数的 Python 库


# 首先，构建命令行输入参数处理 ArgumentParser 实例
parse = argparse.ArgumentParser()
parse.add_argument('file') #输入文件
parse.add_argument(' -o','--output')
parse.add_argument('--width',type = int ,default= 80) # 输出字符画宽
parse.add_argument('--heght',type= int,default= 80)# 画高


#解析并获取参数
args = parse.parse_args()

#输入图片路径
IMG = args.file

#输入字符画的宽度
WIDTH = args.width

#输入字符画的高度
HEIGHT = args.height

# 输出字符画的了路径
OUTPUT =  args.output


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def getchar(r,g,b,alpha = 256):
    #判断alpha的值
    if alpha == 0:
        return ' '
    #获取字符集的长度
    length = len(ascii_char)

    # 将RGB值装换为灰度值 gray 灰度值范围 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    #灰度值范围为0-255 二字符集只要70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1)/length

    return ascii_char[int(gray / unit)]

if __name__ == '__main__':
    #打开并调整图片的宽和高
    im = Image.open(IMG)
    # Image.NEAREST表示输出低质量的图片
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    #初始化输出的字符串
    txt = ''

    #遍历图片中的每一行
    for i in range(HEIGHT):
        #每一列
        for j in range(WIDTH):
            #将(j,i)坐标的RGB像素转化为字符后添加到txt字符串
            # im.getpixel((j,i)) 获取得到坐标 (j,i) 位置的 RGB 像素值（有的时候会包含 alpha 值），返回的结果是一个元组，例如 (1,2,3) 或者 (1,2,3,0)。
            # 我们使用 * 可以将元组作为参数传递给 get_char，同时元组中的每个元素都对应到 get_char 函数的每个参数
            txt += getchar(*im.getpixel((j,i)))
        # 遍历完一行需要增加换行符
        txt += '\n'

    #输出到屏幕
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'W') as f:
            f.write(txt)

    else:
        with open("output.txt",'w') as f:
            f.write(txt)
           



