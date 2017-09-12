#-*-coding:utf-8-*-
#http://cuiqingcai.com/954.html
#设置Headers
#打开一个网页实质上是执行了好多次请求，一般是首先请求HTML文件，然后加载JS，CSS 等等
#用Chrome打开一个网页，F12，点Network，左侧就是html，css，js以及图片等，点一下，右侧则显示具体信息
#拆分这些请求，我们只看一第一个请求，你可以看到，有个Request URL，还有headers，下面便是response
#其中，agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应，所以可以在headers中设置agent,例如下面的例子，这个例子只是说明了怎样设置的headers
import urllib  
import urllib2  

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read() 

#我们还有对付”反盗链”的方式，对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应
#所以我们还可以在headers中加入referer
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' }

#User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
#Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
#application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
#application/json ： 在 JSON RPC 调用时使用
#application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
#在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
#其他的有必要的可以审查浏览器的headers内容，在构建时写入同样的数据即可。

##################################################
#Proxy（代理）的设置
#urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。
#所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
  