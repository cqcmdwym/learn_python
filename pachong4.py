import requests
url = 'http://httpbin.org/get'
data = {'key':'value','abc':'xyz'}
# get是使用get方式请求url，字典型不用进行额外处理
response = requests.get(url,data)
print(response.text)

url = 'http://httpbin.org/post'
response = requests.post(url,data)
#返回json格式
print(response.json())