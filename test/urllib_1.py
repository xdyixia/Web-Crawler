#-*-coding:utf-8-*-
import urllib2
#py3里面urllib和urlib2合并成统一的urllib。Requests是另外的一个库，有更多的功能

#urlopen(url, data, timeout)
#第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间（例timeout=10）。
#第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
#此方法返回一个response对象，response对象有一个read方法

response = urllib2.urlopen("http://www.baidu.com")
print response.read()

#构造request
#urlopen参数可以传入一个request请求，其实就是一个Request的实例，构造时需要传入Url,Data等等的内容
#上面两行代码可以改为下面三行
#运行结果完全一样，只不过中间多了一个request对象，推荐大家这么写，因为在构建请求时通常还需要加入好多内容
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()

#POST和GET数据传送
#上面的程序演示了最基本的网页抓取，不过，现在大多数网站都是动态网页，需要你动态地传递参数给它，它做出对应的响应。
#所以，在访问时，我们需要传递数据给它。最常见的情况是就是登录注册的时候。
#把数据用户名和密码传送到一个URL，然后你得到服务器处理之后的响应
#数据传送分为POST和GET两种方式，最重要的区别是
#GET方式是直接以链接形式访问，链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容。
#POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了，大家可以酌情选择。
#POST方式：
import urllib
values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
#字典定义方式可以改为：values = {}；values['username'] = "1016903103@qq.com"；values['password'] = "XXXX"
#我们需要定义一个字典，名字为values，参数我设置了username和password，下面利用urllib的urlencode方法将字典编码，命名为data，
#构建request时传入两个参数，url和data，运行程序，返回的便是POST后呈现的页面内容。

#GET方式：
#至于GET方式我们可以直接把参数写到网址上面，直接构建一个带参数的URL出来即可。
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
#和我们平常GET访问方式一模一样，这样就实现了数据的GET方式传送。

