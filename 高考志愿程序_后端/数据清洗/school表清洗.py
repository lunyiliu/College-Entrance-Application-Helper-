# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:07:41 2019

@author: admin
"""
import pandas as pd
import pymysql
conn = pymysql.connect(host='39.97.100.184', user='root', passwd='8612260', db='gaokao', charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
from DB_methods import DB_methods
from DB_handler import DB_handler
DBm=DB_methods()
DBh=DB_handler()
#省份ID
province_to_ID=DBm.GetDict(['provinceid'],['省份','ID'],[])
ID_to_province=DBm.GetDict(['provinceid'],['ID','省份'],[])
province_to_ID.pop("' '")
#高考网全体学校
ID_to_name=DBm.GetDict(['gaokaowang_schoolname'],['ID','学校名称'],[])
name_to_ID=DBm.GetDict(['gaokaowang_schoolname'],['学校名称','ID'],[])
school_ID=DBh.select(['school'],['schoolID'],[],para_distinct=True)
gaokaowang_name=[ID_to_name[ID] for ID in school_ID ]
#教育在线全体学校
ecol_name=DBh.select(['ecol_school'],['schoolName'],[],para_distinct=True)
#对比
school_to_update_to_ecol=[]
school_to_insert_to_ecol=[]
for school in gaokaowang_name:
    if school in ecol_name:
        school_to_update_to_ecol.append(school)
    else:
        school_to_insert_to_ecol.append(school)
#找到ecol里需要更新分数和需要插入的学校
school_detail_to_insert=pd.DataFrame(columns=['school','year','province','kelei','pici'])
school_detail_to_update=pd.DataFrame(columns=['school','year','province','kelei','pici','lowest_score','avg_score','highest_score'])
for i,school in enumerate(school_to_update_to_ecol[347:]):
    score_index=cursor.execute("select provinceName,year,subject,pici,lowest_score, avg_score,highest_score from ecol_school where schoolName='%s' "%(school))
    conn.commit()
    rows=list(cursor.fetchall())
    
    for row in rows:
        if row['lowest_score'] is None or row['avg_score'] is None or row['highest_score'] is None :
            row["province"] = row.pop("provinceName")
            row["kelei"] = row.pop("subject")
            row["school"] = school
            school_detail_to_update=school_detail_to_update.append(row,ignore_index=True)
            print('第%d所学校，%s,数据不全:%s,%s,%d,%s'%(i+1,school,row["province"],row["kelei"],row['year'],row['pici']))

    for year in range(2013,2019):
        for province in list(province_to_ID.keys()):
            for kelei in ['literature','science']:
                for pici in ['diyipi','dierpi','tiqianpi','other']:
                    if school_detail_to_update[(school_detail_to_update.year==year) & (school_detail_to_update.school==school) & (school_detail_to_update.province==province) & (school_detail_to_update.kelei==kelei) & (school_detail_to_update.pici==pici)].empty:
                        school_detail_to_insert=school_detail_to_insert.append({'school':school,'year':year,'province':province,'kelei':kelei,'pici':pici},ignore_index=True)
                        print('第%d所学校，%s,需要插入:%s,%s,%d,%s'%(i+1,school,province,kelei,year,pici))

#用高考网的数据更新ecol
school_detail_to_update_final=pd.read_csv('school_detail_to_update_final.csv',encoding='gb2312') 
for row in school_detail_to_update_final.iterrows():
    flag_update=False
    row=row[1]
    gaokao_score=DBh.select(['school'],['lowest_score','avg_score','highest_score'],["schoolID = %s"%name_to_ID[row['school']],"provinceID = %s"%province_to_ID[row['province']],"year = %d"%row['year'],"subject = %s"%row['kelei'],"pici = %s"%row['pici']])
    update_sql="update ecol_school set"
    find_update='发现更新，'
    if not( gaokao_score[0] ==[] and gaokao_score[1] ==[] and gaokao_score[2] ==[]): 
        if type(gaokao_score[0]) is list:
            gaokao_score=[score[0] for score in gaokao_score]               
        if pd.isna(row['lowest_score']) and (gaokao_score[0] is not None):
            flag_update=True
            update_sql+=" lowest_score= %s " %gaokao_score[0] 
            find_update+=" lowest_score= %s " %gaokao_score[0] 
        if pd.isna(row['avg_score']) and (gaokao_score[1] is not None):
            if not flag_update:
                update_sql+=" avg_score= %s " %gaokao_score[1]  
                find_update+=" ,avg_score= %s " %gaokao_score[1]
            else:
                update_sql+=" ,avg_score= %s " %gaokao_score[1]
                find_update+=" ,avg_score= %s " %gaokao_score[1]    
            flag_update=True
        if pd.isna(row['highest_score']) and (gaokao_score[2] is not None):
            if not flag_update:
                update_sql+=" highest_score= %s " %gaokao_score[2]
                find_update+=" highest_score= %s " %gaokao_score[2]
            else:
                update_sql+=" ,highest_score= %s " %gaokao_score[2]
                find_update+=" ,highest_score= %s " %gaokao_score[2]
            flag_update=True
        if flag_update:
            update_sql+=" where schoolName='%s' and provinceName='%s' and year=%d and subject='%s' and pici='%s'"%(row['school'],row['province'],row['year'],row['kelei'],row['pici'])
            cursor.execute(update_sql)
            conn.commit()
            find_update+=",在第%d个学校,%s,%s,%d,%s,%s"%(row['Unnamed: 0'],row['school'],row['province'],row['year'],row['kelei'],row['pici'])
            with open ('update_log.txt','a',encoding='utf-8') as f:
                f.writelines(find_update+'\n')
            print(find_update)
#插入学校
for i,school in enumerate(school_to_insert_to_ecol):
    cursor.execute('select * from school where schoolID=%d'%name_to_ID[school])
    conn.commit()
    rows=cursor.fetchall()
    for row in rows:
        row['schoolName']=ID_to_name[row.pop('schoolID')]
        row['provinceName']=ID_to_province[row.pop('provinceID')]
        print('插入第%d所学校，%s,%s,%d,%s,%s,%s,%s,%s'%(i+1,row['schoolName'],row['provinceName'],row['year'],row['subject'],row['pici'],row['lowest_score'],row['highest_score'],row['avg_score']))
        try:
            DBh.insert('ecol_school',[row['schoolName'],row['provinceName'],row['year'],row['subject'],row['pici'],row['lowest_score'],row['highest_score'],row['avg_score']])
        except Exception as e:
            print(e)
#ecol已经有的学校的插入
school_detail_to_insert_final=pd.read_csv('school_detail_to_insert_final.csv',encoding='gb2312') 
for row in school_detail_to_insert_final.iterrows():
    row=row[1]
    gaokao_score=DBh.select(['school'],['lowest_score','avg_score','highest_score'],["schoolID = %s"%name_to_ID[row['school']],"provinceID = %s"%province_to_ID[row['province']],"year = %d"%row['year'],"subject = %s"%row['kelei'],"pici = %s"%row['pici']])
    find_update='发现插入，'
    if not( gaokao_score[0] ==[] and gaokao_score[1] ==[] and gaokao_score[2] ==[]): 
        if type(gaokao_score[0]) is list:
            gaokao_score=[score[0] for score in gaokao_score]   
        DBh.insert('ecol_school',[row['school'],row['province'],row['year'],row['subject'],row['pici'],gaokao_score[0],gaokao_score[2],gaokao_score[1]])            
        find_update+=",在第%d个学校,%s,%s,%d,%s,%s"%(row['Unnamed: 0'],row['school'],row['province'],row['year'],row['kelei'],row['pici'])
        with open ('insert_log.txt','a',encoding='utf-8') as f:
            f.writelines(find_update+'\n')
        print(find_update)
                      