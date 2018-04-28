__author__ = 'song'
import  sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn=sqlite3.connect('test.db')

# 创建一个Cursor:
cursor=conn.cursor()

# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id VARCHAR(20) PRIMARY key,name varchar(20))')

# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id ,name) VALUES  (\'1\',\'song\')')

# 通过rowcount获得插入的行数:
print(cursor.rowcount)

# 关闭Cursor:
cursor.close()

# 提交事务:
conn.commit()

# 关闭Connection:
conn.close()


#查询
#使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

#使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

#如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
#cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

conne=sqlite3.connect('test.db')

cursor_inq = conne.cursor()

print(cursor_inq.execute('select * from user where id =?',('1',)))

# 获得查询结果集:
values = cursor_inq.fetchall()

print(values)

cursor_inq.close()

conne.close()