# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:46:34 2018

@author: lenovvo
"""
import time
import sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\史老板项目组')
from DB_handler import DB_handler
DB=DB_handler()
command=sys.argv[1]
userID=sys.argv[2]
user_nickname=sys.argv[3]
'''
if command== 'insert_user':
    #找不到条件返回空，目标值是Null的话则是None
    if DB.select(['user'],['user_ID'],["user_ID='%s'"%userID]) ==[]:
        DB.insert('user',["'%s',null,null"%userID])
        print('存入用户ID！')
    else:
        print('在数据库里发现用户！')
	'''	
if command== 'get_school':
    if DB.select(['user'],['user_ID'],["user_ID='%s'"%userID,"user_nickname='%s'"%user_nickname]) ==[]:
        #由于底层的问题，目前只能向数据库里插入字符串null而非真的null
        DB.insert('user',[user_nickname,userID,'null','null',0,0])
    current=DB.select(['user'],['current'],["user_ID='%s'"%userID,"user_nickname='%s'"%user_nickname])
    if current!='null' and current!=None:
        print (current)
    else:
        school=DB.select(['majors'],['学校名称'],['flag_finish is Null'],para_limitation=1)
        DB.update('majors',["flag_finish=2"],["学校名称='%s'"%school])
        DB.update("user",["current='%s'"%school],["user_ID='%s'"%userID,"user_nickname='%s'"%user_nickname])
        print(school)
		
if command== 'get_major':
    #time.sleep(3)
    #print(user_nickname)
    query_list=DB.select(['user'],['current','update_number','insert_number'],["user_ID='%s'"%userID,"user_nickname='%s'"%user_nickname])
    school=query_list[0]
    update_number=query_list[1]
    insert_number=query_list[2]
    _major=DB.select(['majors'],['专业名称','学校名称','录取平均分','录取最高分','省份','科类','年份','批次','一级学科'],['一级学科 is Null',"学校名称='%s'"%school],para_limitation=1)
    if _major[0]!=[]:
        major=_major
    else:
         for i in range(9):		
            print(0)
         print(update_number)
         print(insert_number)                        
         sys.exit()
    if major!=[]:
        #对于数组的返回，请输出单个元素
        for m in major:
            print(m)
    else :
         for i in range(9):		
            print(0)
    print(update_number)
    print(insert_number)
if command== 'next_school':
    school_old=sys.argv[4]
    _major=DB.select(['majors'],['专业名称','学校名称','录取平均分','录取最高分','省份','科类','年份','批次'],['一级学科 is Null',"学校名称='%s'"%school_old],para_limitation=1)
    if _major[0]!=[]:
        major=_major
        for m in major:
          print(m)
    else:
        DB.update('majors',['flag_finish=1'],["学校名称='%s'"%school_old])
        history=DB.select(['user'],['history'],["user_ID='%s'"%userID,"user_nickname='%s'"%user_nickname])
        if history!='null':
            DB.update("user",["history='"+history+","+school_old+"'"],["user_ID='%s'"%userID,"user_nickname='%s'"%user_nickname])
        else:
            DB.update("user",["history='%s'"%school_old],["user_ID='%s'"%userID,"user_nickname='%s'"%user_nickname])
        school_new=DB.select(['majors'],['学校名称'],['flag_finish is Null'],para_limitation=1)
        DB.update("user",["current='%s'"%school_new],["user_ID='%s'"%userID,"user_nickname='%s'"%user_nickname])
        print(school_new)