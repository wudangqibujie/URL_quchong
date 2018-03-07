# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
# md5 = hashlib.md5()
# md5.update('how to wse md5 in '.encode('utf-8'))
# md5.update('的方法玩儿个人格二个人二个人二个人更二个人二二个人更二二哥人lib?'.encode('utf-8'))
# print(md5.hexdigest())


import requests
import hashlib
import random

url = "https://www.doutula.com/article/list/?page=%d"
urls = []
urls_md5 = []
for i in range(10):
    urls.append(url%random.randint(1,5))
for i in urls:
    m = hashlib.md5()
    m.update(i.encode('utf-8'))
    urls_md5.append(m.hexdigest())

print(urls_md5)



