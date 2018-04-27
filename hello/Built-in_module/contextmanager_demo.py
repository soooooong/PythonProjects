__author__ = 'song'
#@contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
#结果，先执行函数tag yield之前内容，再执行with中，再执行yield之后
#<h1>
#hello
#world
#</h1>
#</h1>