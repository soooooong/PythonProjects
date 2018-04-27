__author__ = 'song'

#requests。它是一个Python第三方库，处理URL资源特别方便
#GET
import requests
r = requests.get('https://www.douban.com/') # 豆瓣首页
print(r.status_code)
print(r.text)
#加工url
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
#自动检测编码
print(r.encoding)

#对于特定类型的响应，例如JSON，可以直接获取
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

#需要传入HTTP Header时，我们传入一个dict作为headers参数
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

#POST
#把get()方法变成post()，然后传入data参数作为POST请求的数据
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
