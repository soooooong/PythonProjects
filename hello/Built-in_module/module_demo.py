__author__ = 'song'

#datetime
from datetime import  datetime
da=datetime(2018,4,21,22,23)# 用指定日期时间创建datetime
print(da)
da_stamp=da.timestamp()
print(da_stamp)#将datetime转化为timestamp。timestamp为当前时间相对于epoch time的秒数，epoch time为1970年1月1日 00:00:00 UTC+00:00时区的时刻
da_from_stamp=datetime.fromtimestamp(da_stamp)
print(da_from_stamp)#timestamp转换为datetime

print(datetime.fromtimestamp(da_stamp))#本地时间
print(datetime.utcfromtimestamp(da_stamp))# UTC时间

#str转换为datetime  通过datetime.strptime()实现
from datetime import datetime
cday=datetime.strptime('2018-4-21 22:36:50','%Y-%m-%d %H:%M:%S')
print(cday)
