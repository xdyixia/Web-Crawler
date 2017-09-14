#-*-coding:utf-8-*-
'''
Created on 2017年9月12日

@author: Administrator
'''
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
            'stuid':'1602121103',
            'pwd':'020558'
        })
#登录教务系统的URL
loginUrl = 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fyjsxt.xidian.edu.cn%2Flogin.jsp'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://yjsxt.xidian.edu.cn/electiveForwardAction.do'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()