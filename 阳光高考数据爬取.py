# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 19:30:57 2018

@author: admin
"""
import datetime
import pymysql
from threading import Timer
starttime = datetime.datetime.now()
from urllib.request import urlopen
from bs4 import BeautifulSoup
class TimeoutError(Exception):
    pass
def hello():
    raise TimeoutError()
schoolIDset = []
provinceset = []
yearset = []

for i in range(1, 1872):
    schoolIDset.append(str(i))
for j in range(11, 16):
    provinceset.append(str(j))
for j in range(21, 24):
    provinceset.append(str(j))
for j in range(31, 38):
    provinceset.append(str(j))
for j in range(41, 47):
    provinceset.append(str(j))
for j in range(50, 55):
    provinceset.append(str(j))
for j in range(61, 66):
    provinceset.append(str(j))
for k in range(2014, 2018):
    yearset.append(str(k))

keleiset = [str(1), str(5)]
bset_school = []
for schoolID in schoolIDset[17:1872]:
    #连接到本地mysql数据库
   
    conn = pymysql.connect(host='39.107.97.123', user='root', passwd='123456', db='yangguanggaokaowang', charset='GB2312')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    print("第" + str(schoolID) + "个学校")
    bset_province = []
    for province in provinceset:
       
        bset_year = []
        bset_year.append(province)
        for year in yearset:
            
            if (province == "11" or province == "34"or province == "65"):
                keleiset = [str(11), str(15)]
            else:
                if (province == "31" and year== "2017" or 
                    province == "33" and year== "2017"):
                    keleiset = ["Z"]
                else:
                    if province == "51":
                        keleiset = [str(2), str(6)]
                    else:
                        keleiset = [str(1), str(5)]
            bset_kelei = []
            for kelei in keleiset:
                yang_guang_gao_kao = "http://gaokao.chsi.com.cn/sch/schoolInfoMain.do?schId="+schoolID+"&ssdm="+province+"&lqfsyear="+year+"&kldm="+kelei+"#lqfs"
                html1 = urlopen(yang_guang_gao_kao)
                #t = Timer(10, hello)
                #t.start()
                try:
                    print("A")
                    bs = BeautifulSoup(html1,"lxml")
                    print("B")
                    info = bs.findAll("td", {"class" : "ch-table-center"})
                    p = bs.findAll("option", {"value" : province})
                    b = []
                    b_correct = []
                except TimeoutError as e:
                    print( "超时！")
                    continue
                #t.cancel()
                
                for i in info:
                    b.append(i.get_text())
                    #对数据进行筛选
                for m in b:
                    if (m == "本科提前批" or m == "本专科提前批") :
                        b_correct.append("benke_tiqianpi")
                        b_correct.append(b[b.index(m) + 2])
                    if (m == "本科第一批" or m == "本科一批" or m == "本科第一批（A/B）" or 
                        m == "本科一批（A、B段）" or m == "本科一批（A、A1、B类)" or 
                        m == "本科一批（AB)" or m == "本科第一批(A/B)" or 
                        m == "本科一批、本科一批B" or m == "本科一批（A、B段)"  ):
                        b_correct.append("benke_diyipi")
                        b_correct.append(b[b.index(m) + 2])
                    if (m == "本科批" or m == "本科A批" or m == "普通类" or m == "本科普通批"):
                        b_correct.append("benke_putongpi")
                        b_correct.append(b[b.index(m) + 2])
                    if (m == "本科第二批" or m == "本科二批"):
                        b_correct.append("benke_dierpi")
                        b_correct.append(b[b.index(m) + 2])
                if b_correct != []:
                    bset_kelei.append(b_correct)
                    #准备把这所学校这个省这一年这个科类的信息添加进数据库
                    vinsert=str(schoolID)+','+str(province)+','+"'"+str(kelei)+"'"+','
                    if "benke_tiqianpi" in b_correct : 
                        vinsert=vinsert+str(b_correct[b_correct.index("benke_tiqianpi")+1])+','
                    else:
                        vinsert=vinsert+"NULL,"
                    if "benke_diyipi" in b_correct : 
                        vinsert=vinsert+str(b_correct[b_correct.index("benke_diyipi")+1])+','
                    else:
                        vinsert=vinsert+"NULL,"
                    if "benke_dierpi" in b_correct : 
                        vinsert=vinsert+str(b_correct[b_correct.index("benke_dierpi")+1])+','
                    else:
                        vinsert=vinsert+"NULL,"
                    if "benke_putongpi" in b_correct : 
                        vinsert=vinsert+str(b_correct[b_correct.index("benke_putongpi")+1])
                    else:
                        vinsert=vinsert+"NULL"          
                    sql_="insert into school_"+str(year)+" values( "+vinsert+" )"
                    cursor.execute(sql_)
                    conn.commit()
            if bset_kelei != []:               
                bset_year.append(bset_kelei)
        if bset_year != []:
            bset_province.append(bset_year)
            print("省份编号" + province)                      
    if bset_province != []:
        bset_school.append(bset_province)
    cursor.close()
    conn.close()
endtime = datetime.datetime.now()
print ("用时" + str(endtime - starttime))



    