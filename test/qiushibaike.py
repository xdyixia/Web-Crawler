#-*-coding:utf-8-*-
#抓取糗事百科热门段子
#1.确定URL并抓取页面代码
import urllib
import urllib2
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
#    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        
#2.提取某一页的所有段子
#我们可以看到，每一个段子都是<div class=”article block untagged mb15″ id=”…”>…</div>包裹的内容。
# -*- coding:utf-8 -*-
content = response.read().decode('utf-8')
pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?content">.*?span>(.*?)</span>(.*?)number">(.*?)</i>.*?number">(.*?)</i>',re.S)
items = re.findall(pattern,content)
#for item in items:
#    print item[0],item[1],item[2],item[3],item[4]

#这样我们就获取了发布人，发布时间，发布内容，附加图片以及点赞数。 
#如果不带图片，item[3]获取的内容便是空
#所以我们只需要判断item[3]中是否含有img标签就可以了
#故改进为一下

# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?content">.*?span>(.*?)</span>(.*?)number">(.*?)</i>.*?number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason 

#好啦，现在最核心的部分我们已经完成啦
#接下来可以完善交互，设计面向对象模式参考http://cuiqingcai.com/990.html