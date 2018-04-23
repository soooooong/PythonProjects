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

#datetime 转化为str,使用strftime()
from  datetime import datetime
now=datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

#datetime 加减 使用类timedelta
from  datetime import  datetime,timedelta
now=datetime.now()
print(now)
print(now+timedelta(hours=10)) #现在时间10小时之后
print(now-timedelta(hours=10))
print(now-timedelta(days=2,hours=10))

#时区装换
from datetime import datetime,timedelta,timezone
#1,拿到UTC时间，设置时区为UTC+0(也可以从 其他任何时区作为基准时区转到另一时区)
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#2,装换时区为东八区
db_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(db_dt)