# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:29:42 2018

@author: lenovvo
"""

import requests
import re
import os
import pymysql
import time 
headers = {
    'Connection': 'close',
}
s = requests.session()
s.keep_alive = False
for i in range(107,1601):
    conn = pymysql.connect(host='39.107.97.123', user='root', passwd='123456', db='gaokao', charset='utf8')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql_get_school_name="select 学校名称 from gaokaowang_shcoolname where 学校ID（高考网）="+str(i)
    cursor.execute(sql_get_school_name)
    conn.commit()
    r_=cursor.fetchall()
    if r_==():#学校序号并不是连续的
        continue
    school_name=r_[0]['学校名称']
    dirpath = "C:\\Users\\lenovvo\\Desktop\\史老板项目组\\高校图片\\"+str(school_name)
    url = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1539416399533_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word="+str(school_name)
    html = requests.get(url).text
    urls = re.findall(r'"objURL":"(.*?)"', html)
     
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)
    os.chdir(dirpath) 
    index = 0
    try_times=0
    while index<4:
        print("Downloading: 学校序号:", str(i)," 图片序号：",str(index+1))  
        while 1:
            try:
                res = requests.get(urls[index+try_times],timeout=3)
                break
            except Exception as e:
                print("未下载成功：", url,"错误原因",format(e))
                try_times=try_times+1
        file=" "+str(index)+".jpg"
        with open(file, "wb") as code:
            code.write(res.content)
        index=index+1