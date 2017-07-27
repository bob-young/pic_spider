#coding=utf-8
import time
import re
import codecs
from urllib import request
from bs4 import BeautifulSoup

class htmlpage:
    headers={
       'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
       'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }

    def __init__(self,url,decode='utf-8'):
        self.url=url
        self.decode=decode
        try:
            self.__req=request.Request(self.url,headers=self.headers)
        except ValueError:
            print("incorrect url:%s"%self.url)
            exit()
        try:
            self.web=request.urlopen(self.__req)
        except :
            print("failure to connect to url:%s"%self.url)
            exit()
        self.page=self.web.read()
        self.page=self.page.decode(self.decode)

    def __del__(self):
        print("quit:%s"%self.url)
