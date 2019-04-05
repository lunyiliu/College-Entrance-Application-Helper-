# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:20:45 2019

@author: lenovvo
"""

import pymysql
#====================获取新爬的高考网学校与老数据的异同==================================== 
'''
conn = pymysql.connect(host='39.97.100.184', user='root', passwd='8612260', db='gaokao', charset='utf8')
cursor=conn.cursor()
sql='select distinct 学校名称 from school_copy , gaokaowang_schoolname where gaokaowang_schoolname.ID=school_copy.schoolID '
cursor.execute(sql)
conn.commit()
schools=list(cursor.fetchall())
schools=[school[0] for school in schools]
school_to_add=[]
with open ('C:\\Users\\lenovvo\\Desktop\\school_to_add.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line=line.strip('\n')
        school_to_add.append(line)
school_not_in_copy=[]
school_copy_should_keep=[]
for school in school_to_add:
    if school not in schools:
        school_not_in_copy.append(school)
    else:
        school_copy_should_keep.append(school)
sunshine_schoolID_dictionary={}
with open ('yangguanggaokao_school2ID.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line=line.strip('\n')
        sunshine_schoolID_dictionary[line.split(',')[1]]=line.split(',')[0]
#获取老school表

sql='select distinct 学校名称 from school , gaokaowang_schoolname where gaokaowang_schoolname.ID=school.schoolID '
cursor.execute(sql)
conn.commit()
old_schools=list(cursor.fetchall())
old_schools=[school[0] for school in old_schools]

school_copy_to_delete=[]
old_schools.extend(school_copy_should_keep)
for school in schools:
    if school not in old_schools:
        school_copy_to_delete.append(school)
school_copy_to_delete=[int(sunshine_schoolID_dictionary[school]) for school in school_copy_to_delete]
'''
'''
for school in school_copy_to_delete:
    conn = pymysql.connect(host='39.97.100.184', user='newuser', passwd='liuyilun12345!', db='gaokao', charset='utf8')
    cursor=conn.cursor()
    sql='delete school_copy from school_copy where schoolID=%d'%school
    cursor.execute(sql)
    conn.commit()
'''
#=========================取得训练集========================================
from DB_handler import DB_handler
DBh=DB_handler()
conn = pymysql.connect(host='39.97.100.184', user='root', passwd='8612260', db='gaokao', charset='utf8')
cursor=conn.cursor()
sql='select schoolID,provinceID,year,subject,pici from school where year=2018 and avg_score is not NULL and lowest_score is not NULL and highest_score is not NULL '
cursor.execute(sql)
conn.commit()
results=list(cursor.fetchall())
#元素是：学校，省份，年份，科类，批次
school_prov_year_set=[[result[0],result[1],result[2],result[3],result[4]] for result in results]
five_year_ranks=[]#对应于18年全有的学校-省份集合里元素的其前五年最低分
#获取有五年以上最低分的学校-省份对
for element in school_prov_year_set:
	five_year_rank=DBh.select(['school'],['year','lowest_score'],['schoolID=%d'%element[0],'provinceID=%d'%element[1],'year > 2011','year != 2018','subject=%s'%element[3],'pici=%s'%element[4]],para_OrderBy=['year'])
	if five_year_rank[0]==[]:
		five_year_rank=[]
		five_year_ranks.append(five_year_rank)
	year_set=set(five_year_rank[0])
	if len(year_set)<5:
		five_year_rank=[]
	if None in  five_year_rank[1]:
		five_year_rank=[]        
	if five_year_ranks==[]:
		five_year_ranks=five_year_rank
	else:
		five_year_ranks.append(five_year_rank)
assert len(five_year_ranks)==len(school_prov_year_set)
for i,year_score_set in enumerate(five_year_rank):
	if year_score_set==[]:
		del(five_year_rank[i])
		del(school_prov_year_set[i])
		
		