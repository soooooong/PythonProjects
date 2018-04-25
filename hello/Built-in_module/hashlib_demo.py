__author__ = 'song'

###############################################################
#摘要算法MD5，SHA1等

import hashlib
#MD5
md5=hashlib.md5()
md5.update('11111'.encode('utf-8'))
print(md5.hexdigest())
#hash
sha1=hashlib.sha1()
sha1.update('11111'.encode('utf-8'))
print(sha1.hexdigest())

