def print_arg(str):
    print(str)

def add(a,b):
    print('a ='+a)
    print('b= '+b)
    return a+b
class class_A:
    def __init__(self):
        print('init')
    def fun(self,str):
        print('hello'+str)
        return str

class dedecms_get_webshell:
    def __init__(self):

        self.__run = True

    #nust rewrite function
    def check(self,site,port):
        print('exploiting host %s port %d' % (site,port))
        flag =1
        if flag:
            content={"flag":1,"content":"POST http://www.baidu.com/shell.php (cmd)"}
        else:
            content={"flag":0,"content":"POST http://www.baidu.com/shell.php (cmd)"}
        return content

if __name__=="__main__":
    site="www.baidu.com"
    port=80
    obj = dedecms_get_webshell()
    ret=obj.check(site,port)
    print(ret)