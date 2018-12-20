# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:18:27 2018

@author: lenovvo
"""
import pymysql
import xlrd
ExcelFile=xlrd.open_workbook(r'C:\Users\lenovvo\Desktop\school_rank.xlsx')
sheet=ExcelFile.sheet_by_index(0)
school_name=sheet.col_values(1)
rank=sheet.col_values(0)
conn = pymysql.connect(host='39.107.97.123', user='root', passwd='123456', db='gaokao', charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
for i in range(len(school_name)):
    sql="update gaokaowang_shcoolname set school_rank="+str(rank[i])+"where 学校名称='"+school_name[i]+"'"
    cursor.execute(sql)
    conn.commit()