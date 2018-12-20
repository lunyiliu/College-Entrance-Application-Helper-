# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:51:59 2018

@author: lenovvo
"""

import requests
from lxml import etree
import time
import re
import pymysql
def get_text(content):
    content_text=[]
    for con in content:
        content_text_son=[]
        re_obj1=re.search(u"[\u4e00-\u9fa5]+",con)#专业名称
        content_text_son.append(re_obj1.group())
        con=con[re_obj1.span()[1]:-1]+con[-1]
        re_obj2=re.search(u"[\u4e00-\u9fa5]+",con)#大学名称
        content_text_son.append(re_obj2.group())
        con=con[re_obj2.span()[1]:-1]+con[-1]
        re_obj3=re.search("[0-9]+",con)#平均分
        content_text_son.append(re_obj3.group())
        con=con[re_obj3.span()[1]:-1]+con[-1]
        re_obj4=re.search("[0-9]+",con)#最高分
        content_text_son.append(re_obj4.group())
        con=con[re_obj4.span()[1]:-1]+con[-1]
        re_obj5=re.search(u"[\u4e00-\u9fa5]+",con)#省份
        content_text_son.append(re_obj5.group())
        con=con[re_obj5.span()[1]:-1]+con[-1]
        re_obj6=re.search(u"[\u4e00-\u9fa5]+",con)#科类
        content_text_son.append(re_obj6.group())
        con=con[re_obj6.span()[1]:-1]+con[-1]
        re_obj7=re.search("[0-9]+",con)#年份
        content_text_son.append(re_obj7.group())
        con=con[re_obj7.span()[1]:-1]+con[-1]
        re_obj8=re.search(u"[\u4e00-\u9fa5]+",con)#批次
        content_text_son.append(re_obj8.group())
        con=con[re_obj8.span()[1]:-1]+con[-1]
        content_text.append(content_text_son)
    return content_text
flag_province=1
flag_kelei=1
flag_year=2012
flag_page=1
for provinceID in range(flag_province,32):
    if provinceID!=flag_province:
        flag_kelei=1
    for keleiID in range(flag_kelei,3):
        if keleiID!=flag_kelei:
            flag_year=2012
        for year in range(flag_year,2018):
            if year!=flag_year:
                flag_page=1
            page=flag_page
            while 1:
                url="http://college.gaokao.com/spepoint/a"+str(provinceID)+"/s"+str(keleiID)+"/y"+str(year)+"/p"+str(page)+"/" 
                page=page+1
                while 1: 
                    try:
                        r=requests.get(url,timeout=3.05)
                        break
                    except Exception as e:
                        print("Exception: {}".format(e))
                        time.sleep(5)
                selector=etree.HTML(r.text)
                #“sz”class
                content1_=selector.xpath("//tr[@class='sz']")
                #“szw” class
                content2_=selector.xpath("//tr[@class='szw']")
                if content1_==[] and content2_==[]:
                    break
                content1=[]
                for c in content1_:
                    content1.append(c.xpath('string(.)').strip())

                content2=[]
                for c in content2_:
                    content2.append(c.xpath('string(.)').strip())
                try:
                    content_text1=get_text(content1)
                    content_text2=get_text(content2)
                except Exception as e:
                    print("Exception: {}".format(e))
                    continue
                content_text=content_text1+content_text2
                conn = pymysql.connect(host='39.107.97.123', user='root', passwd='123456', db='gaokao', charset='utf8')
                cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
                for con_text in content_text:
                    sql="insert into gaokaowang_majors values('"+str(con_text[0])+"','"+str(con_text[1])+"',"+str(con_text[2])+','+str(con_text[3])+",'"+str(con_text[4])+"','"+str(con_text[5])+"',"+str(con_text[6])+",'"+str(con_text[7])+"')"
                    cursor.execute(sql)
                    conn.commit()
                print("第"+str(provinceID)+"个省"+"第"+str(year)+"年"+"第"+str(page-1)+"页，科类"+str(keleiID))