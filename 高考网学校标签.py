# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:00:09 2018

@author: lenovvo
"""
import time
import re
from lxml import etree
import requests
import pymysql
for page in range(1,108):
    url="http://college.gaokao.com/schlist/p"+str(page)+"/"
    while 1: 
        try:
            r=requests.get(url,timeout=3.05)
            break
        except Exception as e:
            print("Exception: {}".format(e))
            time.sleep(5)
    selector=etree.HTML(r.text)
    content1_=selector.xpath("//ul")
    content1=[]
    for c in content1_:
        content1.append(c.xpath('string(.)').strip())
    content2_=selector.xpath("//dt")#若要用单斜杠，则必须从起始开始
    content2=[]
    for c in content2_:
        content2.append(c.xpath('string(.)').strip())
    content1_cut=content1[2:27]
    content2_cut=content2[1:26]
    if len(content1_cut)!=len(content2_cut):
        print('长度不相等！')
        while 1:
            pass
    #开始筛选content1
    content1_text=[]
    for con in content1_cut:
        content_text_unit=[]
        re_obj1=re.search(u"[\u4e00-\u9fa5]+：\S+",con)#高校所在地
        con=con[re_obj1.span()[1]:-1]+con[-1]
        re_obj1_content=re.search("(?<=：)\S*", re_obj1.group())#正后发断言
        content_text_unit.append(re_obj1_content.group())
        re_obj2=re.search(u"[\u4e00-\u9fa5]+：\S+",con)#院校特色
        con=con[re_obj2.span()[1]:-1]+con[-1]
        re_obj2_content=re.search("(?<=：)\S*", re_obj2.group())
        content_text_unit.append(re_obj2_content.group())
        re_obj3=re.search(u"[\u4e00-\u9fa5]+：\S+",con)#高校类型
        con=con[re_obj3.span()[1]:-1]+con[-1]
        re_obj3_content=re.search("(?<=：)\S*", re_obj3.group())
        content_text_unit.append(re_obj3_content.group())
        re_obj4=re.search(u"[\u4e00-\u9fa5]+：\S+",con)#高校隶属
        con=con[re_obj4.span()[1]:-1]+con[-1]
        re_obj4_content=re.search("(?<=：)\S*", re_obj4.group())
        content_text_unit.append(re_obj4_content.group())
        re_obj5=re.search(u"[\u4e00-\u9fa5]+：\S+",con)#高校性质
        re_obj5_content=re.search("(?<=：)\S*", re_obj5.group())
        content_text_unit.append(re_obj5_content.group())
        content1_text.append(content_text_unit)
    for i in range(len(content1_text))  :
        content1_text[i].insert(0,content2_cut[i])
    conn = pymysql.connect(host='39.107.97.123', user='root', passwd='123456', db='gaokao', charset='utf8')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    for con_text in content1_text:
        sql="insert into school_attribute values('"+str(con_text[0])+"','"+str(con_text[1])+"','"+str(con_text[2])+"','"+str(con_text[3])+"','"+str(con_text[4])+"','"+str(con_text[5])+"')"
        cursor.execute(sql)
        conn.commit()
    print("第"+str(page)+"页")