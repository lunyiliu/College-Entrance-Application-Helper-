# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:08:06 2018

@author: lenovvo
"""
import requests
from lxml import etree
import re
import pymysql
import time
"""
beautifulsoup 爬取的全是乱码，故用requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
gaokaowang="http://college.gaokao.com/school/tinfo/2/result/5/1/"
html1 = urlopen(gaokaowang)
bs = BeautifulSoup(html1,"html5lib")

一种傻逼的爬取方法
content=[]
content_first=repr(bs.find("tr", {"class" : "sz"}))
for b in bs.find("tr", {"class" : "sz"}).next_siblings: 
    content.append(repr(b))

content_sz=[]
content_szw=[]
info_szw=bs.findAll("tr", {"class" : "szw"})
info_sz=bs.findAll("tr", {"class" : "sz"})
for i in info_sz:
    content_sz.append(i.get_text())
for i in info_szw:
    content_szw.append(i.get_text())
    """
#正则表达式筛选函数
def get_text(content):
    content_text=[]
    for con in content:
        content_text_son=[]
        re_obj1=re.search("[0-9]{4}",con)
        content_text_son.append(re_obj1.group())
        re_obj=[]
        re_obj.append(re_obj1)
        for i in range(1,5):
            con=con[re_obj[i-1].span()[1]:-1]+con[-1]
            re_obj.append(re.search("\S",con))
            if re.search('[0-9]',re_obj[i].group())!=None:
                #如果说有最低分的话
              re_obj[i]=re.search("[0-9]+",con)
              content_text_son.append(re_obj[i].group())
            else:
                content_text_son.append(' ')
                re_obj[i]=re.search("[-]+",con)
        content_text_son.append(con[-3:-1]+con[-1])
        content_text.append(content_text_son)
    return content_text
schoolID_set=[]
provinceID_set=[]
kelei_set=[1,2]
for i in range(1,1601):
    schoolID_set.append(i)
for i in range(1,32):
    provinceID_set.append(i)
provinceID_set+=[33,38,39]
for schoolID in schoolID_set[708:1602]:
    print("学校ID"+str(schoolID))
    for provinceID in provinceID_set:
        print("第"+str(provinceID_set.index(provinceID))+"个省")
        for kelei in kelei_set:
            if kelei==1:
                subject='science'
            else:
				subject='literacy'
			url="http://college.gaokao.com/school/tinfo/"+str(schoolID)+"/result/"+str(provinceID)+"/"+str(kelei)+"/"        
            while 1: 
                try:
                    r=requests.get(url,timeout=3.05)
                    break
                except Exception as e:
                    print("Exception: {}".format(e))
                    time.sleep(5)
            selector=etree.HTML(r.text)
            if selector==None:
                break
            #“sz”class
            content1_=selector.xpath("//tr[@class='sz']")
            content1=[]
            for c in content1_:
                content1.append(c.xpath('string(.)').strip())
            #“szw” class
            content2_=selector.xpath("//tr[@class='szw']")
            content2=[]
            for c in content2_:
                content2.append(c.xpath('string(.)').strip())    
                subject='literature'
            
                
            
            content_text1=get_text(content1)
            content_text2=get_text(content2)
            content_text=sorted(content_text1+content_text2,reverse=True)
            #剔除11年及以前的
            for i in range(len(content_text)):
                if content_text[i][0]=='2011':
                   content_text=content_text[0:i]
                   break
            conn = pymysql.connect(host='39.107.97.123', user='root', passwd='123456', db='gaokao', charset='utf8')
            cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
            if content_text!=[]:
                for con_text in content_text:   
                    sql="insert into school values( "+str(schoolID)+','+str(provinceID)+','+str(con_text[0])+','+"'"+subject+"'"+','+"'"
                    if con_text[5]=='第一批':
                        sql+="diyipi',"
                    else:
                        if con_text[5]=='第二批':
                            sql+="dierpi',"
                        else:
                            if con_text[5]=='提前批':
                                sql+="tiqianpi',"
                            else:
                                sql+="other',"
                    if con_text[1]!=' ':
                        sql+=str(con_text[1])+","
                    else:
                        sql+="NULL,"
                    if con_text[2]!=' ':
                        sql+=str(con_text[2])+","
                    else:
                        sql+="NULL,"
                    if con_text[3]!=' ':
                        sql+=str(con_text[3])+')'
                    else:
                        sql+="NULL)"
                    cursor.execute(sql)
                    conn.commit()