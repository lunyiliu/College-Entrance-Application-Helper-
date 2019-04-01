# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:19:01 2018
@author: lenovvo
"""

import pymysql
class DB_handler:
    #数据库基础操作
    def __init__(self):
        self.conn = pymysql.connect()
        self.cursor=self.conn.cursor()
    def select(self,FormList:"list，从哪几个表中选",ResultList:"list，需要返回哪几个字段的结果",ConditionList:"列表，查询的条件，列表元素格式：XX=XX",para_logic:"哪些条件需要或逻辑,[[xx,value1,value2,...]],[xx,[]]]"=[],para_OrderBy:"第一个元素，排序的字段，第二个元素，true为降序，无为升序"=[],para_dict:"这个参数是true的话，返回的结果是pymysql默认的字典"=False,para_distinct=False,para_limitation:"限制返回的参数个数"=0,para_debug:'此参数开启将打印出sql语句'=False)->"返回的结果是这样的：[[字段1的所有结果],[字段2的所有结果]]，如果字段i只有一条结果的时候，列表将没有嵌套，如果只有一个字段且该字段只有一条结果，则输出一个值":
        #必须由condiyionlist才有para——logic 有点蠢后续在该
        if para_dict==True:
            self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql="select "
        requests = []
        val = []
        mid ={}
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
                if '=' in condition:
                     requests.append(condition.split('=')[0].strip())
                     #print(condition.split('=')[1].strip())
                     val.append(condition.split('=')[1].strip())
                else:
                     condition=condition.strip()
                     request=condition.split(' ')[0].strip()
                     requests.append(request)
                     #print(condition.split('=')[1].strip())
                     mid[request]=condition.split(' ')[1].strip()
                     if mid[request] != 'is':
                         val.append(condition.split(' ')[2].strip())

            if para_logic==[]:
                for request in requests:
                    sql+=str(request)+'= %s'+" and "
                sql = sql.strip(" and ")
            else:
                for request in requests:
                    sql+=str(request)+'= %s'+" and "
                for logic in para_logic:
                    sql = sql +'('
                    column = logic[0] #栏字段名
                    for i in range(len(logic)-1):
                        sql = sql + column + '= %s' + ' or '
                        val.append(logic[i+1])
                    sql = sql.strip(' or ')
                    sql = sql + ')'
                    sql = sql+' and '
                sql = sql.strip(' and ')
        print(val)
        #print(type(val[1]))



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

        self.cursor.execute(sql,val)
        self.conn.commit()
        r_=self.cursor.fetchall()
        if para_dict==True:
            return r_
        if len(ResultList)!=1:
            Result=[]
            if len(r_)!=1:#如果字段i的结果只有一条的话，没有必要嵌套一层列表
                for i in range(len(ResultList)):
                    Result.append([])
                for i in range(len(r_)):
                    for j in range(len(r_[i])):
                        Result[j].append(r_[i][j])
            else:
                Result=list(r_[0])
        else:
            if len(r_)!=1:#如果字段只有一个且其结果只有一条，只返回一个值
                Result=[]
                for i in range(len(r_)):
                    Result.append(r_[i][0])
            else:
                Result=r_[0][0]
        return Result

    def insert(self,form:"要插入的表，str",values:"list，可以是批量（建议批量插入）[[xx，xx，...]，[xx，xx，...]，...]，也可以是一条[xx，xx，xx]"):
        sql="insert into %s values ("%(form)
        if type(values[0]) is list:#多行插入
            for value in values[0]:
                    sql+="%s,"
            sql=sql.strip(",")
            sql+=")"
            print(sql)
            self.cursor.executemany(sql,values)
            self.conn.commit()
        else:
            for value in values:
                    sql+="%s,"
            sql=sql.strip(",")
            sql+=")"
            print(sql)
            self.cursor.execute(sql,values)
            self.conn.commit()

    def update(self,FormList:"str，要更新的表",column:"字符串list，要更新的栏位和值，格式：xx=xx",ConditionList:"列表，更新的条件，列表元素格式：XX=XX",para_logic:"哪些条件需要或逻辑"=[]):
        sql="update "+FormList+" set "
        for col in column:
            sql+= col+','
        sql=sql.strip(",")
        requests = []
        val = []
        if ConditionList!=[]:
            sql+=" where "
            for condition in ConditionList:
                requests.append(condition.split('=')[0].strip())
                #print(condition.split('=')[1].strip())
                val.append(condition.split('=')[1].strip())

            if para_logic==[]:
                for request in requests:
                    sql+=str(request)+'= %s'+" and "
            sql=sql.strip(" and ")
        #sql = sql+';'
        #print(sql)
        #print(val)
        self.cursor.execute(sql,val)
        self.conn.commit()
                
