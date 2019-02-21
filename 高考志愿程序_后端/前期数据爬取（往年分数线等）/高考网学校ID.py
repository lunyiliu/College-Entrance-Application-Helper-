# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:25:13 2018

@author: lenovvo
"""
import pymysql
import requests
import time
from lxml import etree
import re
shcoolID_set=[]
for i in range(1,1601):
    shcoolID_set.append(i)
shcool_dict={}
for shcoolID in shcoolID_set:
    print('第'+str(shcoolID)+'个学校')
    url='http://college.gaokao.com/school/'+str(shcoolID)+'/'
    while 1: 
        try:
            r=requests.get(url,timeout=3.05)
            break
        except Exception as e:
            print("Exception: {}".format(e))
            time.sleep(5)
    selector=etree.HTML(r.text)
    if selector!=None:
        content_=selector.xpath("//h2")
        content=[]
        for c in content_:
            content.append(c.xpath('string(.)').strip())
        shcool_name=re.search(u"[\u4e00-\u9fa5]+",content[0]).group()
        if shcool_name!=None:
            shcool_dict[shcool_name]=shcoolID
conn = pymysql.connect(host='39.107.97.123', user='root', passwd='123456', db='gaokao', charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
'''
for key in shcool_dict:
    print(key)
    sql="insert into gaokaowang_shcoolname values('"+key+"',"+str(shcool_dict[key])+")"
    cursor.execute(sql)
    conn.commit()
    '''