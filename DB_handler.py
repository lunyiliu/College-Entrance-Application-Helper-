# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:19:01 2018

@author: lenovvo
"""

import pymysql
class DB_handler:
    #数据库基础操作
    def __init__(self):
        self.conn = pymysql.connect(host='39.96.168.183', user='root', passwd='123456', db='gaokao', charset='utf8')
        self.cursor=self.conn.cursor()
    def select(self,FormList:"list，从哪几个表中选",ResultList:"list，需要返回哪几个字段的结果",ConditionList:"列表，查询的条件，列表元素格式：XX=XX",para_logic:"哪些条件需要或逻辑"=[],para_OrderBy:"第一个元素，排序的字段，第二个元素，true为降序，无为升序"=[],para_dict:"这个参数是true的话，返回的结果是pymysql默认的字典"=False,para_distinct=False,para_limitation:"限制返回的参数个数"=0,para_debug:'此参数开启将打印出sql语句'=False)->"返回的结果是这样的：[[字段1的所有结果],[字段2的所有结果]]":
        if para_dict==True:
            self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql="select "
        if para_distinct==True:
            sql+="distinct "
        for result in ResultList:
            sql+=result+","
        sql=sql.strip(",")
        sql+=" from "
        for form in FormList:
            sql+=form+","
        sql=sql.strip(",")
        if ConditionList!=[]:
            sql+=" where "
            for condition in ConditionList:
                if para_logic==[]:
                    sql+=condition+" and "
            sql=sql.strip(" and ")
        if para_limitation!=0:
            sql+=" limit "+str(para_limitation)
        if para_OrderBy!=[]:
            for result in ResultList:
                if result==para_OrderBy[0]:
                    sql+=" order by "+result 
                if len(para_OrderBy)==2 and para_OrderBy[1]==True :
                    sql += " desc"
        if para_debug==True:
            print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        r_=self.cursor.fetchall()
        if para_dict==True:
            return r_
        if len(ResultList)!=1:
            Result=[]
            for i in range(len(ResultList)):
                Result.append([])
            for i in range(len(r_)):
                for j in range(len(r_[i])):
                    Result[j].append(r_[i][j])
        else:
            Result=[]
            for i in range(len(r_)):
                Result.append(r_[i][0])
        return Result
    def insert(self,form:"要插入的表，str",values:"list，可以是批量（建议批量插入）[[xx，xx，...]，[xx，xx，...]，...]，也可以是一条[xx，xx，xx]"):
        sql="insert into %s values ("%(form)
        if type(values[0]) is list:
            for value in values[0]:
                    sql+="%s,"
            sql=sql.strip(",")
            sql+=")"
            self.cursor.executemany(sql,values)
            self.conn.commit()    
        else:
            for value in values:
                    sql+="%s,"
            sql=sql.strip(",")
            sql+=")"
            self.cursor.execute(sql,values)
            self.conn.commit()
    def update(self,FormList:"str，要更新的表",column:"字符串list，要更新的栏位和值，格式：xx=xx",ConditionList:"列表，更新的条件，列表元素格式：XX=XX",para_logic:"哪些条件需要或逻辑"=[]):
        sql="update "+FormList+" set "
        for col in column:
            sql+= col+','
        sql=sql.strip(",")
        if ConditionList!=[]:
            sql+=" where "
            for condition in ConditionList:
                if para_logic==[]:
                    sql+=condition+" and "
            sql=sql.strip(" and ")
        self.cursor.execute(sql)
        self.conn.commit()
                
