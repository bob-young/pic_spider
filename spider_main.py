#coding=utf-8
import os
import time
import re
import codecs
from urllib import request
from bs4 import BeautifulSoup


import htmlpage


if __name__=='__main__':
    print("time:")
    print(time.ctime(time.time()))
  
    url=input("url:")
    ac=htmlpage.htmlpage(url)
    print(ac.web.info())

    m_re=r'(//\S+?\.(gif|png|jpg|jpeg))'
    imgs=re.findall(m_re,ac.page,re.I)
    print("picture list:")

    local='./pic_data'
    try:
        os.mkdir(local)
    except:
        print('already exist')
    cnt=0
    imgs=list(set(imgs))
    for i in imgs:
        print(i)
        
        try:
            request.urlretrieve('http:'+i[0],local+'/'+str(cnt)+'.'+i[1])
        except:
            print("http failure!\nnow trying https")
            try:
                request.urlretrieve('https:'+i[0],local+'/'+str(cnt)+'.'+i[1])
            except:
                print("download error")
        
        cnt=cnt+1
    print("\ntotal number:")
    print(len(imgs))
