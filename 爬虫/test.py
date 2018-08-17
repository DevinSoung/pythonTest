#coding:utf-8
import urllib
import re

def get_html(url):
     page = urllib.urlopen(url)
     html = page.read()
     return html

reg = r'src="(.+?\.jpg)" width'#正则表达式
reg_img = re.compile(reg)#编译一下，运行更快
imglist=reg_img.findall(get_html('http://tieba.baidu.com/p/1753935195'))

x = 0
for img in imglist:
     urllib.urlretrieve(img, '%s.jpg' % x)
     x += 1




