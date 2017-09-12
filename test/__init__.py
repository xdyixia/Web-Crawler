#-*-coding:utf-8-*-
'''
Created on 2017年9月12日

@author: Administrator
'''
import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()