# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:47:46 2019

@author: 
"""
from DB_handler import DB_handler
import pymysql
import re
DBh=DB_handler()
ecol_school_and_major=DBh.select(['ecol_majors'],['学校名称','专业名称'],[],para_distinct=True)
ecol_school=list(set(ecol_school_and_major[0]))
error=[]
pattern=re.compile('(学校)|(学院)|(大学)')
for school in ecol_school:
    if not re.search(pattern,school):
        error.append(school)
conn = pymysql.connect(host='39.97.100.184', user='newuser', passwd='liuyilun12345!', db='gaokao', charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute('select 学校名称, AVG(录取平均分) as avg from ecol_majors GROUP BY 学校名称 ORDER BY avg ')
school_score=cursor.fetchall()
error_score={}
for school in error:
    for dic in school_score:
        if school==dic['学校名称']:
            if dic['avg']:
                error_score[school]=int(dic['avg'])
            else:
                error_score[school]=dic['avg']
first_class=DBh.select(['ecol_majors'],['学校名称','专业名称','一级学科','门类'],['年份 = 2017 '],para_distinct=True)
for i in range(len(ecol_school_and_major[0])):
    print('第%d个，在%d个:'%(i+1,len(ecol_school_and_major[0])))
    school=ecol_school_and_major[0][i]
    major=ecol_school_and_major[1][i]
    category=0
    firstclass=0
    if school not in error:
        for j in range (len(first_class[0])):
            if first_class[0][j]== school and first_class[1][j]== major:
                category=first_class[3][j]               
                firstclass=first_class[3][j]
                break
        if category!=0 and firstclass!=0:
            cursor.execute("update ecol_majors set 门类='%s' , 一级学科='%s' where 学校名称='%s' and 专业名称='%s' and 一级学科 is NULL"%(category,firstclass,school,major)) 
            print('更新%s,%s'%(school,major))
            conn.commit()
'''
for school in error_score.items():
    if school[1]==None or school[1]<425 :
        error_to_delete.append(school[0])
for i,school in enumerate(error_to_delete) :
    print(str(i)+'deleting:'+school)
    cursor.execute("delete from ecol_majors where 学校名称 = '%s'"%school)
    conn.commit()
'''